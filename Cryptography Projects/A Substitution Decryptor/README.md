> **Author**: Taylor Murray  
> **Language**: Python 3.10  
> **Tools**: Jupyter Notebook, Standard Python Libraries  
> **Focus**: Cryptography, Classical Cipher Analysis, Algorithm Design

# A Substitution Decryptor (Version 1.0)

## Motivation: 

This project is motivated by Chapter 1 of Understanding Cryptography by **Christof Paar and Jan Pelzl**. 

## What This Project Does:

This project demonstrates how one can utilize basic frequency analysis and elementary python code in decrypting messages  
that have been encrypted by a monoalphabetic substitution cipher. 

### Why it Matters:

- In a world where the development of AI is grouwing at a breakneck pace, information and data are the exceptionally valuable and should be protected against hostile adversaries.
- Understanding how substitution ciphers of can be broken with moderate ease illustrates the necessity of developing stronger ciphers.

### To be Added:
- An encryption function for educational testing 
- A UI for ease of use
- Visualization of letter frequencies using `matlibplot`


## Concepts Used
- Monoalphabetic substitution ciphers
- Letter frequency statistics
- Dictionary manipulation and mapping
- Manual decryption refinement (realistic in practice)
- Bijection enforcement for substitution keys

### Monoalphabetic Substitution Ciphers:

monoalphabetic substitution ciphers are best described by example. Suppose you would like to send a message to your best friend.
However, this friend has a nosy partner who likes reads their private messages. To avoid your friends partner 
in reading messages between you and your friend, you both decide to encrypt messages by using the following key:

|Plaintext|Ciphertext|Plaintext|Ciphertext|
|---------|--------|---------|--------|
|    a    |    c   |    n    |    d   |
|    b    |    e   |    o    |    x   |
|    c    |    f   |    p    |    w   |
|    d    |    a   |    q    |    u   |
|    e    |    z   |    r    |    g   |
|    f    |    t   |    s    |    v   |
|    g    |    s   |    t    |    i   |
|    h    |    q   |    u    |    l   |
|    i    |    o   |    v    |    n   |
|    j    |    k   |    w    |    m   |
|    k    |    b   |    x    |    r   |
|    l    |    y   |    y    |    c   |
|    m    |    p   |    z    |    h   |

For example, if you want to send plaintext (unencrypted) message to your friend:    

"lets get lunch at one",  

you would send your friend the ciphertext (encrypted text):  

"yziv szi yldfq ci udz".  

In turn your friend would use the key above to decrypt the ciphertext into the original
plaintext.

#### A Mathematical Description

Another way to describe a monoalphabetic substitution cipher is through the language of mathematics:
a monoalphabetic substitution cipher is a cipher whose key is a bijection whose domain and codomain is 
your alphabet of choice.

## Project Structure:

The core of the project can be found in `substitution_decryptor.py`

### Features:

- **Frequency Analysis**: Compares frequencies of characters in the ciphertext to English letter frequencies.
- **Initial Key Guessing**: Constructs an initial key from frequency rankings via `initial_possible_key`.
- **Key Refinement**: Easily adjust the key using `old_to_new_key`.
- **Decoded Output**: Presents the evolving message as substitutions improve.

## Installation/Usage Instructions: 

1. Download substitution_decrypter.py
2. Open the file in an IDE such as VS Code or Jupyter Notebooks.
3. Run the code.
4. Use the function `initial_possible_key` on a message you know to be encrypted by a monoalphabetic substitution cipher
    - The function `initial_possible_key` creates a key for decryption based on frequency anlaysis.
5. Use the function `try_possible_key` on the encrypted message and the return of `initial_possible_key` from step 4.
6. Utilize the function `old_to_new_key` to change the decryption key as needed.

## Usage Examples:

Below is an example of an encrypted message example given in **Understanding Cryptography** by Christof Paar and Jan Pelzl. 

``` python

message = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

old_key = try_possible_key(message)

print(try_possible_key(message,key))

```

Output:
``` output
Encrypted Message: 


 lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb


Key Applied to Encrypted Message: 


yecawse the fractnce iu the yasnc mijemeots iu bata ns
the uicws aod masterg iu selu ns the esseoce iu
matswyagashn rgw barate di n shall trg ti elwcndate the
mijemeots iu the bata accirdnop ti mg noterfretatnio
yased io uirtg gears iu stwdg
nt ns oit ao easg tasb ti evflano each mijemeot aod nts
snponuncaoce aod sime mwst remano woevflanoed ti pnje a
cimflete evflaoatnio ioe kiwld haje ti ye xwalnuned aod
nosfnred ti swch ao evteot that he ciwld reach the state
iu eolnphteoed mnod cafayle iu reciponqnop siwodless
siwod aod shafeless shafe n di oit deem mgselu the unoal
awthirntg ywt mg evferneoce knth bata has leut oi diwyt
that the uilliknop ns the frifer afflncatnio aod
noterfretatnio n iuuer mg theirnes no the hife that the
esseoce iu ibnoakao barate knll remano notact
```

We use the old_to_new_key function to change "old_key" based on the output above. For example, the first word in the "decrypted" message looks like it should be "because".
Hence, we should change "l" to "b" and 'n' to 'u'.

``` python

# The above key is not the correct decryption key
# Now call old_to_new_key and make the desired changes to old_key
# Below, we are asking for 'l' to turn into 'b', 'n' to turn into 'u' and so on...

key = old_to_new_key(old_key, { 'l' : 'b', 'n':'u', 's':'p','w':'i', 
                                                    'k':'n', 'x':'f', 'q':'k', 't':'y', 'e':'v',
                                                    'o':'g', 'a':'x', 'g':'z'})

# This key is the correct decryption key
print(try_possible_key(message,key))

```
Output:
``` output

Encrypted Message: 


 lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb


Key Applied to Encrypted Message: 


because the practice of the basic movements of kata is
the focus and mastery of self is the essence of
matsubayashi ryu karate do i shall try to elucidate the
movements of the kata according to my interpretation
based on forty years of study
it is not an easy task to explain each movement and its
significance and some must remain unexplained to give a
complete explanation one would have to be jualified and
inspired to such an extent that he could reach the state
of enlightened mind capable of recognizing soundless
sound and shapeless shape i do not deem myself the final
authority but my experience with kata has left no doubt
that the following is the proper application and
interpretation i offer my theories in the hope that the
essence of okinawan karate will remain intact
```

