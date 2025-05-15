from fingerprint import FingerPrint

# Global configuration
original = None       # Original Finger Print - Will be initialized in main()
max_tries = 15         # Maximum failed attempts allowed, assign your own value.
err_thresh = 0.50     # Minimum matching fraction to grant access, once again use your own value.

def load_fingerprint(filename: str) -> FingerPrint:
    """Read any fingerprintXY.txt (X & Y are numbers) file and return a FingerPrint object."""
    # TODO: Create and return a new FingerPrint object using the filename
    
    pass

def main():
    """Entry point for the interactive application."""
    global original
    
    # TODO: Initialize the original fingerprint from a file
    # Example: original = load_fingerprint("Original.txt")
    
    # TODO: Print information about the original fingerprint
    # Print name, year, rows, cols
    # Print the string representation
    # Print the number of pixels
    # Display the image
    
    # TODO: Load and test at least one other fingerprint
    # Example: user1 = load_fingerprint("data/User1.txt")
    # Print whether it matches the original
    
    # Implement incident response system
    
        # TODO: Part 1 - Implement the logic to prevent users from having more than a certain number of failed attempts.
        
        # TODO: Part 2 - Compare the loaded fingerprint with original using equality
        # Check if fp equals original and respond accordingly
        
        # TODO: Part 3 - Calculate the match percentage and check against threshold
        # Grant access if accuracy >= err_thresh
        
        # TODO: Track attempts and respond appropriately
        # If access granted, break the loop
        # If denied, increment tries and notify user
        
    # TODO: Handle lockout if max_tries is exceeded
    # Print lockout message

if __name__ == '__main__':
    main()