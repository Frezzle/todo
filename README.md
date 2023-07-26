# todo - a CLI task tracker

### Install

No fancy install [yet](https://github.com/Frezzle/todo/issues/3), so just clone the repo and add an alias to your shell's config file:
```sh
alias todo='/path/to/this/repo/todo.py'
```

### Add a task

```
$ todo add demonstrate the app
```

### List tasks

```
$ todo
1 - demonstrate the app
```

### Complete a task

```
$ todo do 1
$ todo
1 - d̶e̶m̶o̶n̶s̶t̶r̶a̶t̶e̶ ̶t̶h̶e̶ ̶a̶p̶p̶
```

### Uncomplete a task

```
$ todo undo 1
$ todo
1 - demonstrate the app
```

### Delete a task

```
$ todo delete 1
$ todo
```
