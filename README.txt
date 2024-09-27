QUIK

https://arqatech.com/ru/support/files/

Externals

https://github.com/wrxck/telegram-bot-lua

Lua

https://www.lua.org/
https://luabinaries.sourceforge.net/index.html - Pre-compiled Lua libraries
- /lua-5.4.2_Win64_bin.zip - Windows x64 Executables 
- /lua-5.4.2_Win64_dllw6_lib.zip - Windows x64 DLL and Includes (MingW-w64 6 Built)
https://github.com/rjpcomputing/luaforwindows - Jan 30, 2018 !!
- Lua for Windows and it's modules all depend on the MSVC++ 2005 runtime library.
https://github.com/luarocks/luarocks/wiki/Installation-instructions-for-Windows

LUA Modules

https://github.com/LewisJEllis/awesome-lua
- /LuaDate - Date and time module with parsing, formatting, addition/subtraction, localization, and ISO 8601 support.

https://luarocks.org/stats/this-week
- https://github.com/golgote/neturl - Parse URL with querystring and build new URL easily
- https://github.com/aiq/basexx - base2(bitfield), base16(hex), base32(crockford/rfc), base64(rfc/url), base85(z85) decoding and encoding.
- https://github.com/kikito/ansicolors.lua - ANSI terminal color manipulation for Lua.
- https://github.com/gvvaughan/lyaml - Lua binding for the fast libYAML C library.
- https://github.com/Tieske/date - 

https://github.com/luarocks
- /argparse - Feature-rich command line parser for Lua

https://github.com/keplerproject - Archived (moved to /lunarmodules - issues with copyrights)
- /rings - Rings is a library which provides a way to create new Lua states from within Lua.
https://github.com/lunarmodules - Modules for the Lua programming language (LuaRocks alternative)
- /luafilesystem - LuaFileSystem is a Lua library developed to complement the set of functions related to file systems offered by the standard Lua distribution.
- /luasql - LuaSQL is a simple interface from Lua to a DBMS.
- /luasocket - Network support for the Lua language
- /luafilesystem - LuaFileSystem is a Lua library developed to complement the set of functions related to file systems offered by the standard Lua distribution.
- /lualogging - A simple API to use logging features in Lua
- /lua-iconv - Lua bindings for POSIX iconv
- /luasec - LuaSec is a binding for OpenSSL library to provide TLS/SSL communication.
- /lua-term - Lua module for manipulating a terminal.
- /lua_cliargs - A command-line argument parsing module for Lua.
- /penlight - Work with common tasks like iterating over directories, reading configuration files and the like.
- /md5 - MD5 offers basic cryptographic facilities for Lua 5.1.
- /copas - Copas is a dispatcher based on coroutines that can be used by TCP/IP servers (uses LuaSocket + LuaSec).

https://github.com/openresty - (NGNIX ecosystem)
- /lua-cjson - Lua CJSON is a fast JSON encoding/parsing module for Lua
- /lua-redis-parser

https://github.com/Olivine-Labs
- /mediator_lua - Mediator pattern implementation for pub-sub management
- /lua-jwt - JSON Web Token library
- /promise - Lua promises
- /lua - The Lua programming language with CMake based build

https://www.tarantool.io/ru/doc/latest/reference/reference_lua/
- /http - HTTP client (https://curl.se/libcurl/ library)
- https://luarocks.org/modules/rtsisyk/http (https://github.com/tarantool/http/tree/tarantool-1.6 - HTTP 1.1 query with no SSL support)

http://lua-users.org/wiki/DateAndTime


================

TL;DR - Lua Lang

- chunks - we call each piece of code that Lua executes (file, line in interactive mode), a sequence of commands (or statements) or a single statement, large chunks (~megabytes) are not a problem for Lua
- Lua is used also as a data-description language
- end-of-file control charter (ctrl-D in POSIX, ctrl-Z in Windows)
- # - length operator, length of a string is its number of bytes
      length of a table is its border (table can be a sequence or not)
      {10, 20, 30, 40, 50} vs {10, 20, 30, nil, 50},
      {} has border 0
- 10 or 20      --> 10
- 10 and 20     --> 20
- 0 or 5        --> 0   -- ( 0 == true)
- "" or 5       --> ""  -- ("" == true)
- local Name <const>] {‘,’ Name <close>]} [‘=’ explist]
- v:name(args)  -- is syntactic sugar for v.name(v,args)
- f{fields}     -- is syntactic sugar for f({fields})
- f'string'     -- is syntactic sugar for f('string')
  f"string"
  f[[string]]
- return functioncall;  -- is called a tail call
  return (f(x))         -- results adjusted to 1
  return 2 * f(x)       -- result multiplied by 2
  return x, f(x)        -- additional results
  f(x); return          -- results discarded
  return x or f(x)      -- results adjusted to 1

function definition
-
  function ‘(’ [parlist] ‘)’ block end
  function Name {‘.’ Name} [‘:’ Name] ‘(’ [parlist] ‘)’ block end
  local function Name ‘(’ [parlist] ‘)’ block end
- 
  function f () body end
  f = function () body end
-
  function t.a.b.c.f () body end
  t.a.b.c.f = function () body end
-
  local function f () body end
  local f; f = function () body end  -- equivalent, supports recursion
 not
  local f = function () body end     -- this only makes a difference when body contains references to f
-

- {...}           -- creates a list with all vararg arguments
- return x, ...   -- returns x and all received vararg arguments
- local x = ...   -- x gets the first vararg argument
- x,y,z = w, f()  -- x gets w, y and z from f()
- {f()}           -- list with all results from f()
- {f(), 5}        -- list with the first !! result from f() and 5

- for Name ‘=’ exp ‘,’ exp [‘,’ exp] do block end
- for i = 1, math.huge do block end
- for var = exp1, exp2, exp3 do block end
- for each value of var from exp1 to exp2, using exp3 as the step to increment var

- for Name {‘,’ Name} in explist do block end
- for var_1, ···, var_n in explist do body end
- var_1 --  control variable
- explist = (1) an iterator function, (2) a state (initial value for the control variable), and (3) a closing value
- var_1, ···, var_n = iterator_function(state, control_variable)
- while var_1 != nill do body()
- do
      local _f, _s, _var = explist
      while true do
          local var_1, ... , var_n = _f(_s, _var)
          _var = var_1
          if _var == nil then break end
          block
      end
  end
- for k in e1, e2, e3 do ... end
