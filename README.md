# todo - a CLI task tracker

### Install

No fancy install yet (#3), so just clone the repo and add an alias to your shell's config file:
```sh
alias todo='/Users/you/todo/todo.py'
```

### Add a task

```
$ todo add clean the code
```

### List tasks

```
$ todo
1 - clean the code
```

### Complete a task

```
$ todo do 1
$ todo
1 - c̶l̶e̶a̶n̶ ̶t̶h̶e̶ ̶c̶o̶d̶e̶
```

### Uncomplete a task

```
$ todo undo 1
$ todo
1 - clean the code
```

### Delete a task

```
$ todo delete 1
$ todo
```
