import logging

class ExtendibleHashing:
    def __init__(self):
        self.current_level = 0
        self.buckets = {0: [], 1: []}  # Two initial buckets
        self.bucket_depths = {0: 0, 1: 0}  # Local depths for each bucket
        self.max_bucket_size = 2  # Maximum number of entries in each bucket

    def hash(self, key):
        # Hash function that uses current level for mod calculation
        return key % (2 ** (self.current_level + 1))

    def insert(self, key, value):
        # Determine bucket index for the given key
        bucket_index = self.hash(key)

        # Ensure the bucket exists
        if bucket_index not in self.buckets:
            self.buckets[bucket_index] = []

        bucket = self.buckets[bucket_index]

        # Insert into the bucket if it has space
        if len(bucket) < self.max_bucket_size:
            bucket.append((key, value))
            print(f"Inserted ({key}, {value}) into bucket {bucket_index}.")
        else:
            # Bucket overflow, need to split
            print(f"Splitting bucket {bucket_index}.")
            self.split_bucket(bucket_index)
            # Reinsert after split to find the correct bucket
            self.insert(key, value)

        # Display the current state after insertion
        self.display()

    # def split_bucket(self, bucket_index):
    #     print(f"Splitting bucket {bucket_index}.")
    #     self.current_level += 1  # Increase the level due to the split

    #     # Create new buckets for the new level
    #     for i in range(2 ** (self.current_level + 1)):
    #         if i not in self.buckets:
    #             self.buckets[i] = []

    #     # Rehash all items in the old bucket
    #     old_items = self.buckets[bucket_index].copy()
    #     self.buckets[bucket_index] = []  # Clear the old bucket

    #     # Reinsert old items into new buckets
    #     for key, value in old_items:
    #         self.insert(key, value)

    def split_bucket(self, bucket_index):
        print(f"Splitting bucket {bucket_index}.")
        
        # Retrieve the local depth for the current bucket
        local_depth = self.bucket_depths[bucket_index]
        
        # Check if we need to increase the global depth
        if local_depth == self.current_level:
            self.current_level += 1
            print(f"Global depth increased to {self.current_level}.")
        
        # Create new buckets for the new level
        for i in range(2 ** (self.current_level + 1)):
            if i not in self.buckets:
                self.buckets[i] = []  # Initialize new buckets
                self.bucket_depths[i] = local_depth + 1  # Set local depth for the new bucket

        # Rehash all items in the old bucket
        old_items = self.buckets[bucket_index].copy()
        self.buckets[bucket_index] = []  # Clear the old bucket

        # Reinsert old items into new buckets based on the new hash values
        for key, value in old_items:
            self.insert(key, value)

        # Increment local depth of the split bucket
        self.bucket_depths[bucket_index] += 1
        print(f"Local depth of bucket {bucket_index} updated to {self.bucket_depths[bucket_index]}.")


    def delete(self, key):
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        initial_size = len(bucket)

        # Remove the key-value pair if found
        self.buckets[bucket_index] = [item for item in bucket if item[0] != key]
        if len(self.buckets[bucket_index]) < initial_size:
            print(f"Deleted key {key} from bucket {bucket_index}.")
        else:
            print(f"Key {key} not found for deletion.")

        # Display the current state after deletion
        self.display()

    def search(self, key):
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]

        print(f"Searching for key {key} in bucket {bucket_index}. Current contents: {bucket}")

        for k, v in bucket:
            if k == key:
                print(f"Found key {key} with value {v} in bucket {bucket_index}.")
                return v

        print(f"Key {key} not found in bucket {bucket_index}.")
        return None

    def display(self):
        print(f"Current state of the Extendible Hash Table:")
        print(f"Current Level: {self.current_level}")
        for index, bucket in self.buckets.items():
            print(f"Bucket {index}: {bucket}")
        print("End of display.\n")

    def statistics(self):
        return {
            'current_level': self.current_level,
            'bucket_count': len(self.buckets),
            'bucket_sizes': {index: len(bucket) for index, bucket in self.buckets.items()}
        }
    
    def get_state(self):
        bucket_sizes = {index: len(bucket) for index, bucket in self.buckets.items()}
        bucket_contents = {index: bucket for index, bucket in self.buckets.items()}
        local_depths = {index: self.bucket_depths.get(index, 0) for index in self.buckets}

        return {
            'current_level': self.current_level,
            'bucket_count': len(self.buckets),
            'bucket_sizes': bucket_sizes,
            'bucket_contents': bucket_contents,
            'local_depths': local_depths,  # Include local depths
        }

# Initialize the ExtendibleHashing instance
extendible_hasher = ExtendibleHashing()
