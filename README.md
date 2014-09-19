brainphrase
===========

Tool for generating high entropy English sentences to be used as pass phrases or as cryptocurrency brain wallets.

Brainphrase is a free open source tool for generating high-entropy
English (or English-like) sentences. It supports generation of 80-bit
entropy sentences and 128-bit entropy sentences. The sentences include
a 9-bit checksum so that if you remember the sentence up to one word,
suggested corrections can be given.

Sentences with 128-bits of entropy can be reasonably used for Bitcoin
brain wallets or the seed for Bitcoin BIP0032 HD wallets.  For the
full 256 bits of entropy one can use two 128 bit sentences in
sequence. An 80-bit entropy sentence is reasonable to use as a
password.

Brainphrase is written in Python and runs under linux.

The 80-bit entropy sentences are all of the form

NP[1] <adverb> <verb> NP[0] <preposition> NP[1]

where NP[i] is either a proper name or of the form

the <i adjectives> <noun>

* Example of an 80 bit sentence:

./genbrainphrase80

> Mrs. Caitlin Woodard powerfully weaves Israel Shaw onto the defensive analysis

./checkbrainphrase80 Mrs. Caitlin Woodard powerfully weaves Israel Shaw onto the defensive analysis

> Valid passphrase

If one word has been forgotten, guess another word that is the same part of speech.
The checksum is used to suggest possible corrections by changing one word.

./checkbrainphrase80 Mrs. Caitlin Woodard powerfully weaves Israel Shaw up the defensive analysis

> Invalid passphrase. Computing possible corrections:
> Mrs. Anna Woodard powerfully weaves Israel Shaw up the defensive analysis
> ...9 lines omitted...
> Mrs. Caitlin Woodard powerfully weaves Israel Shaw onto the defensive analysis
> ...3 lines omitted...

* Example of an 128 bit sentence:

./genbrainphrase128

> the shrill ill leather amid Jorge Houston sternly undid the hard vicious screw via Mrs. Kirsten Griffin

./checkbrainphrase128 the shrill ill leather amid Jorge Houston sternly undid the hard vicious screw via Mrs. Kirsten Griffin

> Valid passphrase

The code for brainphrase was written by Christian Bauer.  Christian's
PGP public key should be included in the file cjbauer.asc.

Thanks to Westin for help writing this README.
