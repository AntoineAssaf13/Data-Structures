Scores={}
import string
for c in string.ascii_lowercase:
    Scores[c]=1
for c in string.ascii_uppercase:
    Scores[c]=2


def lcsScore(A,B,Scores,i=0,j=0,D=None):
    if D == None:
        D = {}
    if i >= len(A) or j >= len(B):
        return ("",0)
    if (i,j) in D:
        return D[(i,j)]
    if not A[i].isalpha():
        return lcsScore(A,B,Scores,i+1, j, D)
    if not B[j].isalpha():
        return lcsScore(A,B,Scores,i, j+1, D)
    if A[i] != B[j]:
        x = lcsScore(A,B,Scores,i+1,j,D)
        y = lcsScore(A,B,Scores,i,j+1,D)
        if x[1] > y[1]:
            D[(i,j)] = x
            return x
        else:
            D[(i,j)] = y
            return y
    else:
        recursiveResult = lcsScore(A,B,Scores,i+1, j+1, D)
        D[(i,j)] = (A[i] + recursiveResult[0] , Scores[A[i]]+recursiveResult[1])
        return D[(i,j)]
S1="""
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou, contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee."""

S2="""  Look in thy glass and tell the face thou viewest
  Now is the time that face should form another;
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose unear'd womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime;
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live, remember'd not to be,
    Die single and thine image dies with thee."""
import sys
sys.setrecursionlimit(2000)
print(lcsScore(S1,S2,Scores))