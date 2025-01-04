#!/usr/bin/env python3

import logging
import os
import sys
from functools import cached_property
from pathlib import Path
from shutil import which
from typing import Dict

import click

from luna.logging.colored import setup_colored_logging
from luna.shellx import fire

log = logging.getLogger(__name__)
parent_dir = Path(__file__).parent


class TfEnv:
    def __init__(self):
        self.env = self.get_env()

    def get_env(self):
        if "TF_ENV" not in os.environ:
            env = "dev"
            log.warning("TF_ENV is not set. Defaulting to: %s", env)
            return env
        env = os.environ["TF_ENV"]
        log.warning("Using environment: %s", env)
        return env

    @cached_property
    def config(self) -> Dict[str, str]:
        import yaml

        env = self.env
        config_path1 = Path.cwd() / f".tfpy.{env}.yaml"
        config_path2 = Path.cwd() / ".tfpy.yaml"
        config_path = config_path1 if config_path1.exists() else config_path2
        if not config_path.exists():
            log.error("Config file not found. Try to create .tfpy.yaml")
            log.info("Example config:")
            with (parent_dir / ".tfpy.sample.yaml").open("r") as f:
                print(f.read())
            sys.exit(1)
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        # render the config
        config = self.render_config(config)
        return config

    def render_config(self, config: Dict[str, str]) -> Dict[str, str]:
        return {k: v.format(env=self.env) if isinstance(v, str) else v for k, v in config.items()}

    @cached_property
    def terraform_bin(self):
        return self.config["terraform_bin"] or which("terraform")

    @property
    def workspace(self) -> Path:
        workspace = self.config["workspace"]
        return Path.cwd() / workspace

    @property
    def conf_data_dir(self):
        data_dir = self.config["data_dir"]
        return (self.workspace / data_dir).resolve().as_posix()

    @property
    def conf_var_file(self):
        var_file = self.config["var_file"]
        return (self.workspace / var_file).resolve().as_posix()

    @property
    def conf_backend_config(self):
        backend_config = self.config["backend_config"]
        return (self.workspace / backend_config).resolve().as_posix()

    def terrafire(self, *cmd, **kwargs):
        cmd = (self.terraform_bin, "-chdir={}".format(self.workspace), *cmd)
        command_env = {**os.environ, "TF_DATA_DIR": self.conf_data_dir}
        log.info("Running: %s", " ".join(cmd))
        try:
            fire(*cmd, env=command_env, cwd=self.workspace, **kwargs)
        except Exception as e:
            log.error("Command failed: %s", e)
            sys.exit(1)

    def init(self, *tf_arguments):
        self.terrafire("init", "--backend-config", self.conf_backend_config, *tf_arguments)

    def plan(self, *tf_arguments):
        self.terrafire("plan", "-var-file", self.conf_var_file, *tf_arguments)

    def apply(self, *tf_arguments):
        self.terrafire("apply", "-var-file", self.conf_var_file, *tf_arguments)

    def destroy(self, *tf_arguments):
        self.terrafire("destroy", "-var-file", self.conf_var_file, *tf_arguments)

    def show(self, *tf_arguments):
        self.terrafire("show", *tf_arguments)

    def output(self, *tf_arguments):
        self.terrafire("output", *tf_arguments)

    def fmt(self, *tf_arguments):
        fire(self.terraform_bin, "fmt", "--recursive", *tf_arguments)

    def generic(self, *tf_arguments):
        self.terrafire(*tf_arguments)


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    tf = TfEnv()
    log.warning("Using config:")
    for k, v in tf.config.items():
        print(f"  {k:<15}:  {v}")
    print()
    ctx.obj = {}
    ctx.obj["tf"] = tf


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def init(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.init(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def plan(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.plan(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def apply(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.apply(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def destroy(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.destroy(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def show(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.show(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def output(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.output(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def fmt(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.fmt(*tf_arguments)


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("tf_arguments", nargs=-1)
@click.pass_context
def generic(ctx, tf_arguments):
    tf: TfEnv = ctx.obj["tf"]
    tf.generic(*tf_arguments)


if __name__ == "__main__":
    setup_colored_logging()
    cli()
