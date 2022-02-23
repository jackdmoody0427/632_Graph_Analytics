In this week's discussion discuss we will discuss ER graphs. Please respond to at least one of the below topics, and reply to two of your classmates’ original responses as well.

- How would you implement generation of ER graph ? Can you treat it as a configuration model ? Can you take advantage of parallel processing in generating ER graph ?

Hey all, sorry for being late to the party!
Much like everyone else has said, you can treat the ER graph as a configuration model. Due to the ER graphs being defined by the Poisson distribution, the degree sequences would be generated from the Poisson distribution and uniformly sampled and connected. Also, theoretically, parallel computing can be used to cut the workload down for each individual computer and get it done faster by dividing and conquering. I'm unsure how that would work in practice though. 
As an aside, this module made me think back to a statistical mechanics class I took in undergrad and I went on a hunt to see if there were any connections between ER graphs and statistical mechanics for materials properties and if there any Monte Carlo Simulations that work with it. I found this really cool paper that goes into it for High Density Percolation. [Statistical mechanics of high-density bond percolation](https://arxiv.org/pdf/1803.03785.pdf)
Best,
Jack Moody 
