syntax on
set autoindent
set number
set mouse=a


set number

syntax on
filetype plugin on

filetype plugin indent on

colorscheme freya

nnoremap <S-F4> :set nonumber!:set foldcolumn=0

map <F5> :w<cr>:!python %<cr>
map <S-F5> :!pyflakes %<cr>

let g:pydiction_location = '~/.vim/ftplugin/pydiction/complete-dict'


