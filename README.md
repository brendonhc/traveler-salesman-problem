# O Problema do Caixeiro Viajante (PCV/TSP)

Um pacote em python para resolver problemas como o do caixeiro viajante, muito conhecido como Traveler Salesman Problem ou pelas siglas TSPs ou PCVs.

Muito simples de utilizar!

## Como utilizar:

- Primeito, basta criar um arquivo de extensão ".tsp" no formato dos arquivos encontrados no diretório [database/](database/) como por exemplo o arquivo [a280.tsp](database/a280.tsp).

- Abra o código [_main.py_](main.py) e logo após os imports é definido um array com o nome de _paths_ como mostra o trecho de código a seguir:
```python
from tsp.tsp import TravelerSalesmanProblem
from tsp.solvers import NearestNeighborSolver, Improver

from datetime import datetime

paths = ['database/brendon.tsp', 'database/brendon2.tsp', 'database/a280.tsp',
         'database/ali535.tsp', 'database/att48.tsp', 'database/att532.tsp',
         'database/berlin52.tsp', 'database/bier127.tsp']

```

- Edite a variável _paths_ sómente com os arquivos que deseja que o código resolva o problema. Se criar um arquivo novo na pasta [database/](database/) com o nome de _meu-exemplo.tsp_ e quiser rodar só ele, a variável paths teria que ser definida assim:
```python
paths = ['database/meu-exemplo.tsp']
```

- Então, com a versão do [_python3_](https://www.python.org/downloads/) instalado na máquina, execute o arquivo _[_main.py_](main.py)_ e veja o relatório impresso no console quanto a solução encontrada para seu(s) problema(s).

## Considerações

Aqui foi exposto uma forma muito simples de  utilizar o pacote, mas, nada te impede de utilizar o pacote para suas próprias aplicações, basta utilizar corretamente as ferramentas desenvolvidas assim como é ilustrado e comentado no código [_main.py_](main.py).

## TODO
### Solução gráfica
A solução gráfica, plotando o roteamento, está em desenvolvimento, há um arquivo _[_main_plot.py_](main_plot.py)_ já com alguns testes, mas, nada definitivo, por isso, não há passo a passo para utilizá-lo ainda. Mas, se desejar contribuir, essa seria uma ótima funcionalidade.
