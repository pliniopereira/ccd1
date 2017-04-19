Manual do usuário do Manager CCD10.

---

<!-- toc -->

  * [Main Window: Overview](#mainwindowoverview)
  * [Conectar](#conectar)
  * [Modos de operação](#modosdeoperação)
    * [Manual](#manual)
    * [Automático](#automático)
  * [Settings](#settings)
    * [System Settings](#systemsettings)
    * [Project Settings](#projectsettings)
    * [Camera Settings](#camerasettings)

<!-- toc stop -->

---
<h1 id="mainwindowoverview">Main Window: Overview</h1>

![Manager CCD10](https://github.com/pliniopereira/ccd10/blob/master/doc/img/CCD_Controller_1.0.0.png)

1. Toolbar para acesso ao File, Connection, Operation Mode e Options.

2. Mostra o horário em Universal Time Coordinated (UTC).

3. Mostra os dados do observatório.

4. Mostra as posições do Sol, Lua e a fase da Lua.

5. Mostra os dados da câmera, bem como o status do sistema de refrigeração e temperatura da CCD.

6. Mostra o status da operação, em verde se estiver em observação, amarelo se estiver em standby e vermelho se apresentar algum erro.

7. Mostra a última imagem tirada.

---

# Conectar
![Conectar](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/menu_conectar.png)

![Conectar](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/Menu_010.png)

> Conecta/desconecta o manager à câmera

---

<h1 id="modosdeoperação">Modos de operação</h1>

![Modos de operação](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/menu_man_aut.png)

![Modos de operação](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/Menu_011.png)

## Manual
> Inicia as observações assim que a CCD atingir a temperatura definida ou que o tempo estabelecido no "CCD Cooling Time" seja satisfeita.

<h2 id="automático">Automático</h2>
> Inicia as observações baseadas nas condições iniciais do Sol e da Lua. Caso as condições sejam satisfeiras as observações iniciação, caso contrário o sistema fica em standby até que as posições do Sol e da Lua atinjam as condições definidas para iniciar as observações.

---

# Settings
![System Settings](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/menu_settings.png)

![System Settings](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/win_settings.png)

<h2 id="systemsettings">System Settings</h2>

![System Settings](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/System%20Settings_019.png)

> Checkbox que define se ao iniciar o Sistema Operacional o Manager inicia automaticamente.

> Definição do local onde serão salvos os logs do Manager.

> Definição do local onde as imagens serão salvas.

<h2 id="projectsettings">Project Settings</h2>

![Project Settings](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/Project%20Settings_020.png)

> Project Name: Define o nome do projeto.

> Site ID: Iniciais do local do observatório, defini o prefixo nome do diretório e do nome da imagem.

> Imager ID: Identificador do Equipamento

> Latitude(°): Define a latitude do observatório.

> Longitude(°): Define a longitude do observatório.

> Elevation(m): Define a altitude em metros do local do observatório.

> Pressure(mb): Define a pressão atmosférica em milibares do local do observatório.

> Temperature(°): Define a temperatura do local do observatório.

> Max Solar Elevation(°): Define a elevação máxima para iniciar as observações

> Ignore Lunar Position: Ignora a posição da Lua no modo automático.

> Max Lunar Elevation(°):Define a elevação máxima para iniciar as observações.

> Max Lunar Phase(%): Define a % da fase da Lua máxima a para iniciar as observações.

> Botão: Save: Salva com os dados dos campos do formulário em arquivo.

> Botão: Clear: Limpa os campos do formulário.

> Botão: Cancel: Fecha a janela sem salvar os dados dos campos do formulário.

<h2 id="camerasettings">Camera Settings</h2>

![Camera Settings](https://raw.githubusercontent.com/pliniopereira/ccd10/master/doc/img/Camera%20Settings_018.png)

### Configurações da camera:
> Temperature(°C): Define a temperatura que a camera deve atingir antes de inicar as observações.

> Filter name: Define o nome do filtro que será utilizado.

> Expusure time: Tempo de exposição.

> Binning: Agrupamento de nxn pixeis para 1x1 pixel.

> Time between photo(s): Intervalo de tempo entre as fotos.

> CCD Cooling Time: Define o tempo mínimo para a camera antigir a temperatura especificada.

> Shooter: Define a condição do obturador: aberto ou fechado.

> Image contrast: bottom level: nível inferior normalizado para ajuste de contraste

> Image contrast: top level: nível superior normalizado para ajuste de contraste

> Botão: Take Photo: Tira uma foto.

> Botão: Set Temp: Envia o comando de temperatura de refrigeração para a CCD.

> Botão: Fan (On/Off): Liga e desliga o sistema de refrigeração.

> Botão: Save: Salva com os dados dos campos em arquivo.

> Botão: Clear: Limpa os campos do formulário.

> Botão: Cancel: Fecha a janela sem salvar os campos modificados.
