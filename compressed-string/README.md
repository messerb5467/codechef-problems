# Description
This problem highlights the need of [decompressing a compressed string](https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!).
The problem wants to focus on automata and is a good chance to focus on some graph-based algorithms where we can implement the graph code manually or rely on networkx for this particular use case just since it is available.

# Benefit-tradeoff analysis of my solution vs the provided solution
Comparing my own solution to the provided solution, mine is much more robust about making sure the data can't change which opens us up to parallel processing capabilities, but this graph in particular has information stored in its edges providing context to the structure of the data which can be hard to do.

Both solutions program to a reasonable level of robustness, but the first one would definitely be nicer stored in a Cloud Function or AWS Lambda than it would be for a backend heavy-lifting script meanwhile mine would not do well in a low latency situation on the front-end. Depending on the complexity of the graph data, it would be time to bring in Neo4J because although we would have to maintain a database, our work parsing the graph data itself would be some much easier. Then we could have different interactions with the database depending on the amount of data coming down the pipe. It would be very interesting to see.
