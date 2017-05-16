## Ecological Functional Genomics 2017

This page contains materials for sessions led by [Stephanie Spielman](sjspielman.org). 


### Helpful resources for biocomputing

Many of these resources go beyond the scope of this workshop, but all are incredibly useful for your future endeavors in biocomputing!

+ The [Unix Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/) is a great resource and starting point for getting comfortable with the command-line environment. 
+ [Software Carpentry](https://software-carpentry.org/lessons/) offers lots of open-source lessons and tutorials for scientific computing skills (github, Python, command line, R, SQL, and more!)
+ [Google](google.com) is easily the most valuable resource for figuring things out. If you encounter an issue, chances are somebody else has also encountered it and has asked about it. 

 > Protip: Google your error messages and look for links to [Stack Overflow](http://www.stackoverflow.com) answers. This forum-based website has all the answers (but they might be snarky).
+ The popular websites [Code Academy](http://www.codecademy.com/), [Rosalind](http://rosalind.info/problems/locations/), and [Lynda](https://www.lynda.com/Programming-Languages-training-tutorials/) have some great materials for learning Python and practicing bioinformatics skills. You will need university credentials to access Rosalind and Lynda, so check to see if your institution gives you access.
+ Some papers that are helpful if/when you dive into the world of programming:
  + [An Introduction to Programming for Bioscientists: A Python-Based Primer](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004867)
  + PLoS journals have some great gems:
      + **Scientific Computing in General:** [Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
      + **Version control:** [Ten Simple Rules for Taking Advantage of Git and GitHub
](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
      + **Software development**: [Ten Simple Rules for Developing Usable Software in Computational Biology](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005265)
      + **Data storage**: [Ten Simple Rules for Digital Data Storage
](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005097)
		+ **Reproducible research**: [Ten Simple Rules for Reproducible Computational Research
](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)


### May 25th: Detecting selection in protein-coding sequences

Given a *multiple sequence alignment* containing protein-coding sequences and a corresponding *phylogeny*, what kinds of questions can we ask?

+ Is my gene subject to positive selection?
+ Is my gene subject to positive selection on a specific set of branches?
+ Are specific sites in my gene subject to positive selection?
+ Do certain lineages experience shifts (increased or decreased intensity) in selection pressure?

We will learn about to address these and related questions using [HyPhy](http://hyphy.org), via the [Datamonkey webserver](datamonkey.org).
> Note: Newer analyses like BUSTED, aBSREL, and RELAX, are only available via the [development Datamonkey webserver](test.datamonkey.org).

### May 26th: Introduction to Computing


Many of today's exercises come from the **excellent** book [Practical Computing for Biologists](http://practicalcomputing.org) by Haddock and Dunn. This book is a thorough, entry-level overview of introductory computing concepts, showcased with hands-on exercises. The book's accompanying website (linked above) is also regularly updated with important tips, examples, and errata.


Basic concepts to cover:

+ Navigating your computer
+ Using the command line
+ Regular expressions
+ (Brief!) introduction to concepts in programming
