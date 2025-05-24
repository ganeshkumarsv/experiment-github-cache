import datetime
import os

def main():
    # Create cache directory if it doesn't exist
    os.makedirs('cache', exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.datetime.now().isoformat()
    
    # Write timestamp to cache file
    with open('cache/timestamp.txt', 'w') as f:
        f.write(timestamp)
    
    print(f"Generated timestamp: {timestamp}")

if __name__ == "__main__":
    main() 