# Stipo

**Year:** 2023

**Owner:** Abdullayev Doston

**Platform:** Linux

## Introduction

Welcome to Stipo, a simple yet powerful tool for command logging on Linux systems. This documentation will guide you through the installation, usage, and features of Logger, helping you make the most of this valuable logging tool.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Commands](#commands)
5. [Stopping Stipo](#stopping-stipo)
6. [Examples](#examples)
7. [Advantages & Disadvantages](#advantages--disadvantages)

## Getting Started

Logger is designed to help you keep a record of commands executed on your Linux system. It allows you to easily track and document your activities for auditing, debugging, or reference purposes.

## Installation

To install Stipo, follow these steps:

1. Clone the Stipo repository from GitHub:

    ```bash
    git clone https://github.com/offensivecyber03/stipo.git
    ```

2. Change your working directory to the Logger directory:

    ```bash
    cd stipo
    ```
3. Install requirements:
    ```bash
    pip3 install -r requirements.txt
    ```
    
4. You can use python script or make the Logger script executable:

    ```bash
    chmod +x stipo
    ```

5. You can add the Logger directory to your system's PATH to run it from anywhere without specifying the path:

    ```bash
    export PATH=$PATH:$(pwd)
    ```

## Usage

Stipo is designed to be user-friendly and provide valuable insights into your command execution history. You can start and stop logging at any time, change the working directory, and execute commands as needed.

## Commands

Stipo accepts the following commands:

- `log -start`: Start logging.
- `log -stop`: Stop logging.
- `exit`: Exit.

## Stopping Stipo

To stop Stipo, simply run:

```bash
log -stop
```
# Examples

Example of output

![Screenshot from 2023-10-01 16-41-18](https://github.com/offensivecyber03/logger/assets/71892943/a3d54907-b5e7-4bf1-99b0-80f3034b04b7)


# Advantages & Disadvantages
Advantages:
Capable of capturing log with output

Capable of capturing log with user info, time and location

Capable of capturing more conveinent and easy to read output with .html extension

For security, tool will save output to /root directory when tool starts by root user.

Disadvantages:
Couldn't support when user changes made

Couldn't support commands when response doesn't end like: tool calling from terminal (firefox, remmina, terminal and etc), commands with asking extra options such as asking confirmation, password, flag and etc.

Couldn't support when terminal splits or changes

Tool intended to use confidential operations and works.
