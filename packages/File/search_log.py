def search_log(log_file, search_keyword):
    try:
        # Open the log file in read mode
        with open(log_file, 'r') as file:
            for line in file:
                # Check if the search keyword is present in the line
                if search_keyword in line:
                    # If found, display the line
                    # Using strip to remove newline character
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Test the function
log_file = "sample_log.txt"
search_keyword = "ERROR"
search_log(log_file, search_keyword)
