def license(me, agents, others):
    client_queue = sorted(others.split() + [me])[::-1]
    time = 20

    while True:
        for i in range(agents):
            curr_client = client_queue.pop()

            if curr_client == me:
                return time

        time += 20



print(license("Zebediah", 1, "Bob Jim Becky Pat"))
