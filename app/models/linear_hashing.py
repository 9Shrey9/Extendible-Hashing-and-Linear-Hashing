import logging


class LinearHashing:
    def __init__(self):
        self.size = 2  # Number of buckets
        self.count = 0  # Number of entries in the hash table
        self.load_factor_threshold = 0.75  # Load factor threshold for rehashing
        self.bucket_capacity = 2  # Maximum capacity of each bucket
        self.buckets = [[] for _ in range(self.size)]  # Initialize buckets
        self.next_bucket_to_split = 0  # Pointer to the next bucket to split

    def hash(self, key):
        """A simple hash function that uses the modulo operator."""
        return key % self.size

    def load_factor(self):
        """Calculate the current load factor based on total capacity."""
        total_capacity = self.size * self.bucket_capacity  # Total bucket capacity
        return self.count / total_capacity

    # def insert(self, key, value):
    #     """Insert a key-value pair into the hash table."""
    #     # Check the load factor and split before inserting the new element.
    #     while self.load_factor() >= self.load_factor_threshold:
    #         self.split_bucket()  # Split the next bucket if load factor exceeds threshold

    #     index = self.hash(key)

    #     # Check for duplicates
    #     if not any(item[0] == key for item in self.buckets[index]):
    #         # Allow up to bucket_capacity entries in each bucket
    #         if len(self.buckets[index]) < self.bucket_capacity:
    #             self.buckets[index].append((key, value))
    #             self.count += 1
    #             logging.info(f"Inserted ({key}, {value}) into bucket {index}.")
    #         else:
    #             logging.warning(f"Bucket {index} is full. Cannot insert ({key}, {value}).")
    #     else:
    #         logging.warning(f"Key {key} already exists in bucket {index}.")

    #     # Print the current bucket contents to the terminal
    #     self.display()
    #     return self.statistics()

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        # Check the load factor and split before inserting the new element.
        while self.load_factor() >= self.load_factor_threshold:
            self.split_bucket()  # Split the next bucket if load factor exceeds threshold

        index = self.hash(key)

        # Check for duplicates
        if not any(item[0] == key for item in self.buckets[index]):
            # Allow up to bucket_capacity entries in each bucket
            if len(self.buckets[index]) < self.bucket_capacity:
                self.buckets[index].append((key, value))
                self.count += 1
                logging.info(f"Inserted ({key}, {value}) into bucket {index}.")
            else:
                logging.warning(
                    f"Bucket {index} is full. Cannot insert ({key}, {value})."
                )
                # If the bucket is full, it will try to split the bucket first
                self.split_bucket()  # Try to split the bucket
                self.insert(key, value)  # Retry the insertion
        else:
            logging.warning(f"Key {key} already exists in bucket {index}.")

        # Print the current bucket contents to the terminal
        self.display()
        return self.statistics()

    # def split_bucket(self):
    #     """Split the next bucket in the table to manage overflow."""
    #     bucket_index = self.next_bucket_to_split
    #     logging.info(f"Splitting bucket {bucket_index}.")

    #     # Create a new bucket to add
    #     self.buckets.append([])  # Add an extra bucket
    #     self.size += 1  # Increase the size of the hash table

    #     old_items = self.buckets[bucket_index].copy()
    #     self.buckets[bucket_index] = []  # Clear the old bucket

    #     # Move entries from the old bucket to the appropriate buckets
    #     for key, value in old_items:
    #         new_index = self.hash(key)
    #         if new_index != bucket_index:
    #             self.buckets[new_index].append((key, value))
    #         else:
    #             self.buckets[bucket_index].append((key, value))

    #     # Move to the next bucket to split
    #     self.next_bucket_to_split += 1

    #     # Update next_bucket_to_split to wrap correctly
    #     if self.next_bucket_to_split >= self.size:  # Adjust to correct bounds
    #         self.next_bucket_to_split = 0

    #     # Print the state after the split
    #     self.display()

    def split_bucket(self):
        """Split the next bucket in the table to manage overflow."""
        bucket_index = self.next_bucket_to_split
        logging.info(f"Splitting bucket {bucket_index}.")

        # Create a new bucket to add
        self.buckets.append([])  # Add an extra bucket
        self.size += 1  # Increase the size of the hash table

        old_items = self.buckets[bucket_index].copy()
        self.buckets[bucket_index] = []  # Clear the old bucket

        # Move entries from the old bucket to the appropriate buckets
        for key, value in old_items:
            new_index = self.hash(key)
            if new_index != bucket_index:
                self.buckets[new_index].append((key, value))
            else:
                self.buckets[bucket_index].append((key, value))

        # Move to the next bucket to split
        self.next_bucket_to_split += 1
        if self.next_bucket_to_split >= self.size:  # Cycle back to the start
            self.next_bucket_to_split = 0

        # Print the state after the split
        self.display()

    def delete(self, key):
        """Remove a key from the hash table."""
        index = self.hash(key)
        bucket = self.buckets[index]

        # Check if the key is present in the bucket
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                self.count -= 1
                logging.info(f"Deleted key {key} from bucket {index}.")
                self.display()
                return self.statistics()

        logging.warning(f"Key {key} not found for deletion in bucket {index}.")
        self.display()
        return self.statistics()

    def search(self, key):
        """Search for a key in the hash table."""
        index = self.hash(key)
        bucket = self.buckets[index]

        logging.info(
            f"Searching for key {key} in bucket {index}. Current contents: {bucket}"
        )
        for item in bucket:
            if item[0] == key:
                logging.info(f"Found key {key} in bucket {index} with value {item[1]}.")
                return item[1]

        logging.warning(f"Key {key} not found in bucket {index}.")
        return None

    def display(self):
        """Display the current state of the hash table."""
        print("\n=== Current State of the Linear Hash Table ===")
        print(f"Current size: {self.size}")
        print(f"Next bucket to split: {self.next_bucket_to_split}")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")
        print("=== End of Current State ===\n")

    def statistics(self):
        """Return statistics about the hash table."""
        return {
            "current_size": self.size,
            "entry_count": self.count,
            "load_factor": self.load_factor(),
            "bucket_sizes": {
                index: len(bucket) for index, bucket in enumerate(self.buckets)
            },
        }

    def get_state(self):
        """Get the current state of the hash table."""
        load_factor = self.load_factor()
        bucket_sizes = {i: len(self.buckets[i]) for i in range(self.size)}
        bucket_contents = {i: self.buckets[i] for i in range(self.size)}

        return {
            "current_size": self.size,
            "entry_count": self.count,
            "load_factor": load_factor,
            "bucket_sizes": bucket_sizes,
            "bucket_contents": bucket_contents,
        }


# Initialize the LinearHashing instance
linear_hasher = LinearHashing()
