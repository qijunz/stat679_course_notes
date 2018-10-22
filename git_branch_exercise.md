## git branch notes

### Creating a new branch:

```
git branch new-branch    # creates a branch
git branch               # lists the existing branches
git checkout new-branch  # switches the current branch
git branch
```

<<<<<<< HEAD
#### Student A creates new branch A
=======
#### Student B creates a new branch B
>>>>>>> b8c0657a947b86d1bd1e3b7a6af06afd3cea8812

#### Greeting from student A modifing branch B

<<<<<<< HEAD
#### Student A creates a new branch A
=======
#### Greeting from student B modifing branch A

#### Student B creates a new branch B
>>>>>>> 91df28ac0f71e516d9aa5c992e9fb9b0bf79e235

#### Greeting from student A using pulled branch B
