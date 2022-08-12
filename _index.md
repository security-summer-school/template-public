# SSS TODO-track-name

This is the public repository for the **TODO-track-name** track of the Security Summer School (SSS).
It contains information available to participants: session content, slides, activities support files.
Apart from SSS participants, you can use this content by yourself to learn more about **TODO-track-name**.

## Using the Content

As with all SSS tracks, the **TODO-track-name** track consists of multiple sessions.
One session typically covers a particular topic of the track.
Ideally you would go through the sessions orderly, but you can jump ahead to a topic of interest.

Each session has its own folder.
The `index.md` file from a session folder details the topic of the session and includes practical demos of tools and snippets of code.

A typical activity will challenge you to solve / exploit a given issue and obtain a flag.
Read the activity description in the session contents and then use the activity support file to get to a solution.
Each activity will develop your practical skills and help you get a better understanding of the session topics.

Activities come in two forms:

- **tutorials**: that provide a step-by-step detailing of the solution.
- **challenges**: that only state the goal and provide an initial scaffolding (and maybe some hints), then the rest is up to you.
  Even so, challenge activity folders store the reference solution for you to take a sneak peak in case you're lost.

## Support

In case you have questions or want to know more about a topic, use the `Discussions` tab or join the [SSS Discord community](https://bit.ly/DiscordSecuritySummerSchool).

## Sessions

The sessions of the SSS **TODO-track-name** track are:

- [Session 01: Name](session-name-1/index.md)
- TODO
- TODO

### Session Folder Structure

A session folder consists of:

- `index.md`: session contents, written in [GitHub Markdown](https://guides.github.com/features/mastering-markdown/)
- `activities/`: each activity has its own folder with support files (including the reference solution)
- `assets/`: support files for session contents (images, diagrams, code snippets, demos, packet captures, etc.)
- `slides/`: support files for session slides presentation.
  It should include a `Makefile` that uses `common/slides.mk` and generates slides using [reveal-md](https://github.com/webpro/reveal-md).

### Activity Folder Structure

An activity folder consists of:

- `README.md`: contains the challenge name, hints, vulnerability overview, solution overview.
- `flag`: contains the flag string.
- `public/`: stores public files that are to be packed in an archive that is to be made available to participants.
  They are usually generated from the `src/` folder, though they may also be static files.
- `sol/`: holds the reference solution of the activity.
- `src/` (optional): stores similar contents to a CTF challenge.
  The generated files that are to be made available to participants will be stored in the `public/` folder in the corresponding activity folder in the public repository.
  Most activities require a source code folder, but some may not, making the `src/` folder optional.
- `deploy/` (optional): stores similar contents to a CTF challenge.
  Most activities require remote deployment in a Docker container, but some may not, making the `deploy` folder optional.
  It typically consists of the following files:

  - `Dockerfile`: for creating the Docker container that will run the challenge on the remote system.
  - `docker-compose.yml`: for configuring the Docker containers.
  - `.dockerignore`: for [excluding](https://docs.docker.com/engine/reference/builder/#dockerignore-file) some files from the Docker container.
  - `Makefile`: for building and running Docker containers.
    This file should include `common/activity.mk` in most cases, but if a challenge has a different structure it can implement its own Makefile.
    For the general Makefile we have the following commands:
    - `make run`: start the Docker container.
    - `make build`: build the Docker image.
    - `make generate`: generate the file with the flag from `../flag`.
    - `make stop`: stop the container.
    - `make clean`: remove the image, the container and the generated file.
  - `run.sh` (when required): Docker startup script, used to start services.
    It's used inside the `Dockerfile` with `COPY + CMD` commands.
  - Additional files required for the deployment.
    They may be static files or files generated from the `src/` folder.

The `session-name-1/activities/activity-folder-1/` folder contains scaffolding contents of an activity folder:

```
|-- deploy/
|   |-- .dockerignore
|   |-- docker-compose.yml
|   |-- Dockerfile
|   |-- Makefile
|   `-- run.sh
|-- flag
|-- README.md
|-- sol/
|   `-- README.md
`-- src/
    `-- index.template.php
```

## Contributing

Contributions are welcome.
See the [contribution guide](CONTRIBUTING.md) on how you could report or fix issues and on how you can improve the content.

Reviewers are requested to follow the [reviewing guide](REVIEWING.md).

For in-depth discussions, please join the [SSS Discord community](https://bit.ly/DiscordSecuritySummerSchool).
