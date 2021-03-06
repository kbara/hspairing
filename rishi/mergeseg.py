#!/usr/bin/env python
from collections import deque

def merge(segments):
    starts_merged = {}
    ends_merged = {}
    for (segstart, segend) in segments:
        # This is the tricky case: joining two known paths
        if segstart in ends_merged and segend in starts_merged: 
            start_path = ends_merged[segstart]
            end_path = starts_merged[segend]
            start_path.extend(end_path)
            merged_path = start_path # misomner
            
            # update the start/end to point to the merged path
            starts_merged[merged_path[0]] = merged_path
            ends_merged[merged_path[-1]] = merged_path
            # delete the stale start/end
            del ends_merged[segstart]
            del starts_merged[segend]
        elif segstart in ends_merged:
            current_path = ends_merged[segstart]
            current_path.append(segend)
            ends_merged[segend] = current_path
            del ends_merged[segstart] # no longer a path end
        elif segend in starts_merged:
            current_path = starts_merged[segend]
            current_path.appendleft(segstart)
            starts_merged[segstart] = current_path
            del starts_merged[segend] # no longer a path start
        else:
            starts_merged[segstart] = deque([segstart, segend])
            ends_merged[segend] = starts_merged[segstart] # This *shares* the deques

    return map(lambda x:''.join(x), starts_merged.values()) 

    
def arePathsSane(paths):
    chars = set()
    for p in paths:
        for c in p:
            chars.add(c)
    num_chars = sum(map(len, paths))
    num_uniq = len(chars)
    return num_chars == num_uniq

