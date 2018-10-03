## homework-10-03 solution

### For task

Run the following command line in the directory containing `tableofSNPs.csv` file:

```
sed '2,$ s/\"/''/g' tableofSNPs.csv | sed '2,$ s/,/''/2' > tableofSNPs_new.csv
```

The first part of command `sed '2,$ s/\"/''/g'` replace `"` to empty charater (kind of removing original character) in each row.  

The second part of command `sed '2,$ s/,/''/2'` remove the second `,` character in each row (except first row - column names)

After running, the modified table will be stored in `tableofSNPs_new.csv` file.

To check if every row in the modified file has 3 commas, run the following command line:

```
sed 's/[^,]//g' tableofSNPs_new.csv | wc -lm
```

The **output contains two numbers**, first one is the number of total lines, and the second number is the number of total characters.

The first part of command `sed 's/[^,]//g' tableofSNPs_new.csv` remove all characters besides `,` in `tableofSNPs_new.csv` file. 

the second part of command `wc -lm` calculate the number of total lines and total characters.

If the number of total characters is 4 times greater than the number of total lines (e.g, the output is `10 40`), indicating in the modified file has 3 commas in each row.

### For extra task

Run the following command line in the directory containing the new modified `tableofSNPs_new.csv` file:

```
sed -e 's/A/T/g' -e 's/T/A/g' tableofSNPs_new.csv > tableofSNPs_new_recovered.csv
```

After running, the recovered table will be stored in `tableofSNPs_new_recovered.csv` file.

To check if the command works correctly, run: 

```
wc tableofSNPs_new.csv
```

and 

```
wc tableofSNPs_new_recovered.csv
```

If the outputs of two command are same, the recovered file have the same lines, words, and characters numbers with the original file, indicating the command works.  
