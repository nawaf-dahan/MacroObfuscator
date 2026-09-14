#!/usr/bin/env python3
"""
MacroObfuscator - VBA Macro Obfuscation Tool
Designed for cybersecurity research and security analysis.
Built using Pure Python (Standard Library Only).
"""

import os
import sys
import re
import json
import random
import string
import logging
import argparse

VERSION = "1.0.0"

# Initialize Logging System
logger = logging.getLogger("MacroObfuscator")

def setup_logging(level_str):
    """Setup log level based on user choice"""
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    log_level = levels.get(level_str.upper(), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

def load_config(config_path):
    """Load configuration file if present with error handling"""
    default_config = {
        "rename_variables": True,
        "encode_strings": True,
        "strip_comments": True,
        "variable_prefix": "v_"
    }
    if not config_path:
        return default_config

    if not os.path.exists(config_path):
        logger.error(f"Configuration file does not exist: {config_path}")
        sys.exit(1)

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            user_config = json.load(f)
            default_config.update(user_config)
            logger.info(f"Configuration successfully loaded from: {config_path}")
            return default_config
    except json.JSONDecodeError:
        logger.error(f"Configuration file is corrupted or invalid JSON: {config_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to read configuration file: {str(e)}")
        sys.exit(1)

def generate_random_name(prefix="v_", length=8):
    """Generate a random variable name"""
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"{prefix}{random_str}"

def encode_string_to_chr(match):
    """Convert strings into VBA Chr() function representations"""
    text = match.group(1)
    if not text:
        return '""'
    chr_arr = [f"Chr({ord(c)})" for c in text]
    return " & ".join(chr_arr)

def obfuscate_vba(code, config):
    """Main core logic for obfuscating VBA code"""
    result = code

    # 1. Strip Comments and Empty Lines
    if config.get("strip_comments", True):
        # Remove comments starting with ' or Rem (without touching strings)
        result = re.sub(r"(?m)^\s*('|\bRem\b).*$", "", result)
        result = re.sub(r"[\r\n]{2,}", "\n", result) # Remove duplicate empty lines
        logger.debug("Comments and empty lines successfully removed.")

    # 2. Encode Strings to Chr()
    if config.get("encode_strings", True):
        # Search for strings enclosed in double quotes "text"
        result = re.sub(r'"([^"\n]*)"', encode_string_to_chr, result)
        logger.debug("Strings successfully encoded into Chr() format.")

    # 3. Rename Variables and Functions
    if config.get("rename_variables", True):
        # Reserved VBA keywords to prevent replacement
        keywords = {
            "sub", "function", "dim", "as", "string", "integer", "long", "boolean",
            "if", "then", "else", "end", "next", "for", "to", "loop", "do", "while",
            "set", "new", "object", "nothing", "true", "false", "autoopen", "document_open"
        }
        
        # Extract variables defined after Dim
        dim_vars = re.findall(r"(?i)\bDim\s+([a-zA-Z_][a-zA-Z0-9_]*)", result)
        prefix = config.get("variable_prefix", "v_")
        
        var_map = {}
        for var in set(dim_vars):
            if var.lower() not in keywords:
                var_map[var] = generate_random_name(prefix)

        for old_var, new_var in var_map.items():
            result = re.sub(r"\b" + re.escape(old_var) + r"\b", new_var, result)
            
        logger.debug(f"Successfully renamed {len(var_map)} variables.")

    return result

def main():
    parser = argparse.ArgumentParser(
        description="VBA Macro code obfuscation tool for security research and testing purposes (MacroObfuscator)."
    )
    
    parser.add_argument("-i", "--input", help="Path to input VBA Macro file")
    parser.add_argument("-o", "--output", help="Path to save output obfuscated file")
    parser.add_argument("--config", help="Path to JSON configuration file (optional)")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO", help="Log verbosity level (Default: INFO)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}", help="Show program version")

    args = parser.parse_args()

    # Setup Logging
    setup_logging(args.log_level)

    # Check essential input
    if not args.input:
        logger.error("No input file specified! Use -i or --help option for details.")
        sys.exit(1)

    input_path = os.path.abspath(args.input)

    # Handle file existence and permissions errors
    if not os.path.exists(input_path):
        logger.error(f"Specified file does not exist: {input_path}")
        sys.exit(1)

    if not os.path.isfile(input_path):
        logger.error(f"Specified path is not a file: {input_path}")
        sys.exit(1)

    # Load configuration
    config = load_config(args.config)

    # Read file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            vba_code = f.read()
            logger.info(f"File read successfully ({len(vba_code)} characters).")
    except PermissionError:
        logger.error(f"Permission denied to read file: {input_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)

    # Perform Obfuscation
    logger.info("Executing obfuscation process...")
    obfuscated_code = obfuscate_vba(vba_code, config)

    # Determine output path
    output_path = args.output
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_obfuscated{ext}"

    # Write output
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
            logger.info(f"Obfuscated file saved successfully to: {output_path}")
    except PermissionError:
        logger.error(f"Permission denied to write to path: {output_path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred while saving the file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()