# Enable aliases to be sudo’ed
alias sudo='sudo '

alias ..="cd .."
alias ...="cd ../.."
alias ll="ls -l"
alias la="ls -la"
alias ~="cd ~"
alias dotfiles="cd '$DOTFILES_PATH'"

# Fusion
source $HOME/.dotfiles/shell/aliases/fusion.sh

# Jumps
source $HOME/.dotfiles/shell/aliases/jumps.sh

# Git
source $HOME/.dotfiles/shell/aliases/git.sh

# Utils
source $HOME/.dotfiles/shell/aliases/utils.sh
