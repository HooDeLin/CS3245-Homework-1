This is the README file for A0126576X's submission

== Python Version ==

I'm using Python Version 2.7 for
this assignment.

== General Notes about this assignment ==

Give an overview of your program, describe the important algorithms/steps 
in your program, and discuss your experiments in general.  A few paragraphs 
are usually sufficient.

To build the language model, we get the 4-gram from the trained input and put it into a dictionary.
The language model dictionary would have this structure:
{
    "language A":
        {(ngram-A): occurence of ngram-A, ......, (ngram-N): occurence of ngram-N },
    ......,
    "language N":
        {......}
}

Note that we do not insert probability. This is because when we are reading the train data line by line,
we would not know how many ngrams we are able to generate. To fix this problem, there is another component
of the language model which records the counts of ngrams. It would have this structure:
{
    "language A": # of ngrams,
    ......,
    "language N": # of ngrams,
}

To predict the language, we calculate the probability of each language. We determine the final
language by looking at the language that has the highest probability. To tackle language that are
Malay, Indonesian, Tamil, we check the percentage of unfound ngrams in the input sentence. Currently,
the threshold is set at 80%. If 80% of the ngrams are not found in our language model, we treated it
as other languages.

== Files included with this submission ==

List the files in your submission here and provide a short 1 line
description of each file.  Make sure your submission's files are named
and formatted correctly.

build_test_LM.py: python script that builds the language model and generate predictions from text files
README.txt: This file

== Statement of individual work ==

Please initial one of the following statements.

[X] I, A0126576X, certify that I have followed the CS 3245 Information
Retrieval class guidelines for homework assignments.  In particular, I
expressly vow that I have followed the Facebook rule in discussing
with others in doing the assignment and did not take notes (digital or
printed) from the discussions.  

[ ] I, A0126576X, did not follow the class rules regarding homework
assignment, because of the following reason:

N/A

I suggest that I should be graded as follows:

N/A

== References ==

N/A