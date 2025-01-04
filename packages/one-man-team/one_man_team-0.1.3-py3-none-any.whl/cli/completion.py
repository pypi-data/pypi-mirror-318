import click

COMPLETION_SCRIPT = '''
_omt_completion() {
    local IFS=$'\n'
    local response

    response=$(env COMP_WORDS="${COMP_WORDS[*]}" COMP_CWORD=$COMP_CWORD _OMT_COMPLETE=bash_complete $1)

    for completion in $response; do
        IFS=',' read type value <<< "$completion"
        if [[ $type == 'dir' ]]; then
            COMPREPLY=()
            compopt -o dirnames
        elif [[ $type == 'file' ]]; then
            COMPREPLY=()
            compopt -o default
        elif [[ $type == 'plain' ]]; then
            COMPREPLY+=($value)
        fi
    done

    return 0
}

_omt_completion_setup() {
    complete -o nosort -F _omt_completion omt
}

_omt_completion_setup;
'''

ZSH_SCRIPT = '''
#compdef omt

_omt() {
    local -a completions
    local -a completions_with_descriptions
    local -a response

    response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _OMT_COMPLETE=zsh_complete $words[1])}")

    for type key descr in ${response}; do
        if [[ "$type" == "plain" ]]; then
            if [[ "$descr" == "" ]]; then
                completions+=("$key")
            else
                completions_with_descriptions+=("$key:$descr")
            fi
        elif [[ "$type" == "dir" ]]; then
            _path_files -/
        elif [[ "$type" == "file" ]]; then
            _path_files -f
        fi
    done

    if [ -n "$completions_with_descriptions" ]; then
        _describe -V unsorted completions_with_descriptions
    fi

    if [ -n "$completions" ]; then
        compadd -U -V unsorted -a completions
    fi
}

compdef _omt omt
'''

FISH_SCRIPT = '''
function __fish_omt_complete
    set -l response (env _OMT_COMPLETE=fish_complete COMP_WORDS=(commandline -cp) COMP_CWORD=(commandline -t) omt)

    for completion in $response
        set -l type (string split --max 1 , $completion)[1]
        set -l value (string split --max 1 , $completion)[2]

        switch $type
            case 'plain'
                echo $value
            case 'dir'
                __fish_complete_directories $value
            case 'file'
                __fish_complete_path $value
        end
    end
end

complete -c omt -a "(__fish_omt_complete)"
'''

@click.group()
def completion():
    """Shell completion commands"""
    pass

@completion.command()
@click.option('--shell', type=click.Choice(['bash', 'zsh', 'fish']), default='bash',
              help='Shell type for completion script')
def show(shell):
    """Show completion script"""
    if shell == 'bash':
        click.echo(COMPLETION_SCRIPT)
    elif shell == 'zsh':
        click.echo(ZSH_SCRIPT)
    elif shell == 'fish':
        click.echo(FISH_SCRIPT)
    else:
        click.echo('Unsupported shell')

@completion.command()
@click.option('--shell', type=click.Choice(['bash', 'zsh', 'fish']), default='bash',
              help='Shell type for completion script')
def install(shell):
    """Install completion script"""
    if shell == 'bash':
        # 写入到 ~/.bashrc
        import os
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path, 'a') as f:
            f.write('\n# OMT completion\n')
            f.write(COMPLETION_SCRIPT)
        click.echo(f'Completion script installed to {bashrc_path}')
        click.echo('Please restart your shell or run:')
        click.echo('source ~/.bashrc')
    elif shell == 'zsh':
        # 写入到 ~/.zshrc
        import os
        zshrc_path = os.path.expanduser('~/.zshrc')
        with open(zshrc_path, 'a') as f:
            f.write('\n# OMT completion\n')
            f.write(ZSH_SCRIPT)
        click.echo(f'Completion script installed to {zshrc_path}')
        click.echo('Please restart your shell or run:')
        click.echo('source ~/.zshrc')
    elif shell == 'fish':
        # 写入到 ~/.config/fish/completions/omt.fish
        import os
        fish_path = os.path.expanduser('~/.config/fish/completions/omt.fish')
        os.makedirs(os.path.dirname(fish_path), exist_ok=True)
        with open(fish_path, 'w') as f:
            f.write(FISH_SCRIPT)
        click.echo(f'Completion script installed to {fish_path}')
        click.echo('Fish completion is ready to use') 