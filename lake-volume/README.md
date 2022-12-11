# Description
The purpose of this (problem)[https://techdevguide.withgoogle.com/resources/former-interview-question-volume-of-lakes/#!] is to be handed an array of data and calculate how much water the lakes will retain vs how much would drain out.

This forces us to practice Big-O notation, generalization, efficiency, time and space complexity, and anticipating edge cases.

# Prerequisites
For preprocessing the data, please convert it to flatfile using np.savetxt. It will save a lot of time in any data preprocessing moves. Here's how to convert it below:
    ```
    import numpy as np
    conv_array = np.array(<list_to_save>)
    np.savetxt('lake-elev-data.txt', conv_array)
   ```

# Assumptions
For the complexity of this function, doing parallel processing is not worth it. I usually approach things with a what would this look like
in production setting and if we were to do that, I would definitely need to treat the `find_lakes` algorithm with minimally a python generator to keep it the most efficient for small data and a bigger stream processor like Spark or Kafka if I'm getting hit with huge amounts of data. Choice of programming language even would be best spent on how big the data would be and what tools we would have available at our disposal.

# Notices
The algorithm was very good and was sourced from [Google's own tech interview lake volume solution]([https://techdevguide.withgoogle.com/resources/former-interview-question-volume-of-lakes/#!]). After careful review of my own work and it in a competitive code review, I used their work as it made more sense for the problem being drawn and will be good to have as a handy reference.
