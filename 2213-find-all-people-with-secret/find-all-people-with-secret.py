class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known_people_set = set([0, firstPerson])

        # Sort meetings based on time
        sorted_meetings = []
        meetings.sort(key=lambda x: x[2])

        # Use a set to keep track of seen times
        seen_time = set()

        # Group meetings by time
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        # Traverse each meeting group
        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)

            # Build a graph and identify people who already know the secret
            for person1, person2 in meeting_group:
                graph[person1].append(person2)
                graph[person2].append(person1)
                if person1 in known_people_set:
                    people_know_secret.add(person1)
                if person2 in known_people_set:
                    people_know_secret.add(person2)

            # Use BFS to find all connected people who know the secret
            queue = deque(people_know_secret)

            while queue:
                current_person = queue.popleft()
                known_people_set.add(current_person)
                for neighbor in graph[current_person]:
                    if neighbor not in known_people_set:
                        known_people_set.add(neighbor)
                        queue.append(neighbor)

        # Return the final list of people who know the secret
        return list(known_people_set)