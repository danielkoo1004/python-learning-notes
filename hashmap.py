def new(num_buckets = 16):
    """Initializes Map with given size of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """Given a key a number is created and converted to index for aMap's buckets."""
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Given a key, find the bucket."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default = None):
    """
    Returns the index, key and value of slot found in a bucket.
    Returns -1, key and default when not found.
    """
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    return -1, key, default

def get(aMap, key, default = None):
    """Gets value in bucket for given key."""
    i, k, v = get_slot(aMap, key, default = default)
    return v

def set(aMap, key, value):
    """Sets key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

def delete(aMap, key):
  """Deletes key from the Map."""
  bucket = get_bucket(aMap, key)

  for i in xrange(len(bucket)):
      k, v = bucket[i]
      if key == k:
          del bucket[i]
          break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
       if bucket:
           for k, v in bucket:
               print(k, v)
