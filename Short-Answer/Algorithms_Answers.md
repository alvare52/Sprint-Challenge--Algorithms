#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) - complexity scales with input size n


b) Linearithmic O(n log n) - halving (log n) inside of a linear function O(n)


c) Linear O(n) - complexity scales with input size n

## Exercise II

    ####  }
    ####  }
    ####  } - n floors
    ####  }
    ####  }

    start at midpoint, throw eggs, see if they break
    if they do, find new midpoint on floors below and keep doing it until the eggs dont break

    if floor <= n:
        # try again
    else:
        egg_broke == False
    
    Runtime Complexity - O(log n)
    
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

