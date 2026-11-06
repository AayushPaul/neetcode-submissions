class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #U: Identical tasks must be separated by >= n CPU cycles to cooldown the CPU. 
            # Return min number of CPU cycles to complete all tasks 

        #M/P: Max Heap
            # Convert tasks to a max heap 
            # The task with the highest frequency will be popped first (it's the root)
            # Create empty queue (FIFO) to store pairs: 
                # (remaining_count_after_running, next_available_time) 
            # time = 0 
            # While (!heap) 

        #I: 
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time