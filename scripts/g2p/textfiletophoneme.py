import subprocess
import argparse

def run_phonetise_script(script_path, input_file):
    # Run the phonetise_Buckwalter.py script with the input file
    result = subprocess.run(['python', script_path, input_file], capture_output=True, text=True)

    # Print the output and any errors
    print("Output:")
    print(result.stdout)
    print("Errors:")
    print(result.stderr)

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Run a specific phonetise_Buckwalter.py script on the specified input file.")
    parser.add_argument('script_path', type=str, help="Path to the phonetise_Buckwalter.py script")
    parser.add_argument('input_file', type=str, help="Path to the input file")

    args = parser.parse_args()

    # Call the function with the script path and input file arguments
    run_phonetise_script(args.script_path, args.input_file)
