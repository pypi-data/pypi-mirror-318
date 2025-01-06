![](https://i.imgur.com/y6hOYx3.png)
This is a library that makes automating events in ADOFAI levels more convenient.
<br>List of Classes:<br>
<hr>
<i><code style="color : white">LevelDict</code></i>
<dl>
    Initalize with <code>LevelDict(filename, encoding)</code>.<br>
    Creates a blank LevelDict if <code>filename</code> is left blank.<br>
    <code>encoding</code> defaults to utf-8-sig.<br>
    <br><dt><code>LevelDict.filename : str</code>
    <dd>The filename of the file from which the <code>LevelDict</code> was obtained.
    <dt><code>LevelDict.encoding : str</code>
    <dd>The encoding of the file from which the <code>LevelDict</code> was obtained.
    <dt><code>LevelDict.nonFloorDecos : list[Decoration]</code>
    <dd>A list of all decorations in the level that are not tied to any particular tile.
    <dt><code>LevelDict.settings : Settings</code>
    <dd>The level settings, as a Settings object.
    <dt><code>LevelDict.tiles : list[Tile]</code>
    <dd>A list of all tiles in the level. (See <code>Tile</code> class)</dd>
    <hr><dt><code>LevelDict.appendTile(angle : float) -> None:</code>
    <dd>Adds a single tile to the end of the level.
    <dt><code>LevelDict.appendTiles(angles : list[float]) -> None:</code>
    <dd>Adds a list of tiles to the end of the level.
    <dt><code>LevelDict.insertTile(angle : float, index : int) -> None:</code>
    <dd>Adds a single tile to the level before the specified index.
    <dt><code>LevelDict.insertTiles(angles : list[float], index : int) -> None:</code>
    <dd>Adds a list of tiles to the level before the specified index.
    <dt><code>LevelDict.getAngles() -> list[float]:</code>
    <dd>Returns a list of angles for each tile.
    <dt><code>LevelDict.setAngles(angles: list[float]) -> None:</code>
    <dd>Writes a list of angles to angleData. The list is truncated if it's too big, and the track is truncated if the list is too small.
    <dt><code>LevelDict.getAnglesRelative(ignoretwirls: bool=False, padmidspins: bool=False) -> list[float]</code>
    <dd>Gets a list of relative angles (degrees between each pair of tiles.) Twirls are taken into account by default. To disable this, set ignoretwirls to True. If padmidspins is set to True, midspin values (999) are replaced with 0 instead of being removed in order to keep the list the same length. Midspins are always taken into account.
    <dt><code>LevelDict.setAnglesRelative(angles: list[float]) -> None</code>
    <dd>Sets a list of relative angles (degrees between each pair of tiles.)
    <dt><code>LevelDict.addAction(event : Action) -> int:</code>
    <dd>Adds the given action to the level. Returns the index of the event within the tile.
    <dt><code>LevelDict.addDecoration(event : Decoration) -> int:</code>
    <dd>Adds the given decoration to the level. Returns the index of the event within the tile / within the list of non-floor decorations.
    <dt><code>LevelDict.getActions(condition : Callable) -> list[Action]:</code>
    <dd>Returns a list of actions in the level that meet the given condition. Returns a list of all actions if condition is not specified.
    <dt><code>LevelDict.getDecorations(condition : Callable) -> list[Decoration]:</code>
    <dd>Returns a list of decorations in the level that meet the given condition. Returns a list of all decorations if condition is not specified.
    <dt><code>LevelDict.removeActions(condition : Callable) -> list[Action]:</code>
    <dd>Removes all actions in the level that meet the given condition. Returns a list of removed actions.
    <dt><code>LevelDict.removeDecorations(condition : Callable) -> list[Decoration]:</code>
    <dd>Removes all decorations in the level that meet the given condition. Returns a list of removed decorations.
    <dt><code>LevelDict.popAction(tile, index) -> Action:</code>
    <dd>Removes the action at the specified tile at the specified index. Returns the event.
    <dt><code>LevelDict.popDecoration(tile, index) -> Decoration:</code>
    <dd>Removes the decoration at the specified tile at the specified index. Returns the event.
    <dt><code>LevelDict.replaceFieldAction(condition : Callable, field : str, new) -> None:</code>
    <dd>Changes the value of "field" to "new" in all actions that meet the given condition.
    <dt><code>LevelDict.replaceFieldDecoration(condition : Callable, field : str, new) -> None:</code>
    <dd>Changes the value of "field" to "new" in all decorations that meet the given condition.
    <dt><code>LevelDict.writeDictToFile(leveldict : dict, filename : str):</code>
    <dd>Writes the given dictionary to the specified file. Overwrites the original file if filename is not specified.
    <br><i>Use this if you are working with <code>LevelDict.leveldict</code>.</i>
    <dt><code>LevelDict.writeToFile(filename : str=None) -> None:</code>
    <dd>Writes the level to the specified file. Overwrites the original file if filename is not specified.
</dl>
<hr>
<i><code style="color : white">Settings</code></i><br>
Part of a LevelDict object. A <code> Settings</code> object behaves like a <code>dict</code>. The keys of this dictionary are equivalent to the parameters in the <code>settings</code> field of a .adofai file.
<hr>
<i><code style="color : white">Tile</code></i><br>
A list of Tiles is contained within a LevelDict object.
<dl>
    <dt><code>Tile.angle : float</code>
    <dd>The angle that the tile points towards (0 degrees is facing right, 90 degrees is facing upwards)
    <dt><code>Tile.actions : list[Action]</code>
    <dd>A list of actions which are present on that particular tile.
    <dt><code>Tile.decorations : list[Decoration]</code>
    <dd>A list of decorations which are present on that particular tile.
</dl>
<hr>
<i><code style="color : white">Action</code></i><br>
An event that goes on a tile (one with a purple icon). An <code> Action </code> object behaves like a <code>dict</code>. The keys depend on the event type. Check any entry in the <code>actions</code> field of a .adofai file for more information on the fields used by that event type.
<br><br>
Action objects are found in a list of actions in a <code>Tile</code> object.
<hr>
<i><code style="color : white">Decoration</code></i><br>
A decoration, object decoration, or text decoration (anything found in the decorations menu on the left sidebar). A <code> Decoration</code> object behaves like a <code>dict</code>. The keys depend on the event type. Check any entry in the <code>decorations</code> field of a .adofai file for more information on the fields used by that event type.
<br><br>
Decoration objects are found in a list of decorations in a <code>Tile</code> object. If the decoration is not tied to any tile, it is found in the list of non-floor decos.
<hr><br>

이 라이브러리는 ADOFAI 커스텀 레벨 제작 중 코딩을 통한 이벤트 자동생성을 편리하게 하기 위해 존재합니다.
<br>클래스 소개:<br>
<hr>
<i><code style="color : white">LevelDict</code></i>
<dl>
    <code>LevelDict(filename, encoding)</code>을 통해 객체를 초기화합니다.<br>
    <code>filename</code>(파일 이름, .adofai 형식의 JSON 파일)을 입력하지 않을 경우 비어있는 LevelDict를 생성합니다.<br>
    <code>encoding</code>(인코딩)의 기본값은 utf-8-sig입니다.<br>
    <br><dt><code>LevelDict.filename : str</code>
    <dd><code>LevelDict</code>로부터 가져온 filename입니다.
    <dt><code>LevelDict.encoding : str</code>
    <dd><code>LevelDict</code>로부터 가져온 encoding입니다.
    <dt><code>LevelDict.nonFloorDecos : list[Decoration]</code>
    <dd>어떤 타일에도 속하지 않는 모든 장식의 리스트입니다.
    <dt><code>LevelDict.settings : Settings</code>
    <dd>레벨 설정을 Settings 오브젝트로서 나타냅니다.
    <dt><code>LevelDict.tiles : list[Tile]</code>
    <dd>레벨의 모든 타일의 리스트입니다. (<code>Tile</code> 클래스를 확인하세요.)</dd>
    <hr><dt><code>LevelDict.appendTile(angle : float) -> None:</code>
    <dd>레벨의 끝에 타일을 하나 추가합니다.
    <dt><code>LevelDict.appendTiles(angles : list[float]) -> None:</code>
    <dd>레벨의 끝에 리스트 형태의 타일들을 추가합니다.
    <dt><code>LevelDict.insertTile(angle : float, index : int) -> None:</code>
    <dd>지정된 인덱스 직전에 타일을 하나 추가합니다.
    <dt><code>LevelDict.insertTiles(angles : list[float], index : int) -> None:</code>
    <dd>지정된 인덱스 직전에 리스트 형태의 타일들을 추가합니다.
    <dt><code>LevelDict.getAngles() -> list[float]:</code>
    <dd>각 타일의 각도를 리스트 형태로 반환합니다.
    <dt><code>LevelDict.setAngles(angles: list[float]) -> None:</code>
    <dd>리스트 형태의 각도들을 angleData(ADOFAI 커스텀 레벨 파일에서, 타일을 저장하는 부분)에 적용합니다. LevelDict.tiles의 크기와 리스트의 크기가 다른 경우 두 값이 같아지도록 더 큰 쪽(타일 또는 각도의 리스트)의 뒷부분을 슬라이싱합니다. 
    <dt><code>LevelDict.getAnglesRelative(ignoretwirls: bool=False, padmidspins: bool=False) -> list[float]</code>
    <dd>상대각도(근접한 두 타일 사이의 각도)의 리스트를 반환합니다. 기본적으로 소용돌이를 고려하고 계산됩니다. 소용돌이를 무시하기 위해선 ignoretwirls를 True로 세팅하세요. 미드스핀(오각형 타일)을 항상 고려하고 계산됩니다.
    <dt><code>LevelDict.setAnglesRelative(angles: list[float]) -> None</code>
    <dd>리스트 형태의 상대각도들을 angleData에 적용합니다. LevelDict.setAngles와 동일한 적용방식을 가집니다.
    <dt><code>LevelDict.addAction(event : Action) -> int:</code>
    <dd>주어진 Action(오브젝트)을 레벨에 추가합니다. 해당 이벤트가 있는 타일에서의 이벤트의 인덱스(.adofai 파일은 이벤트에 인덱스를 부여하지 않으며, 이 인덱스는 LevelDict에서 임의로 지정하는 인덱스입니다)를 반환합니다.
    <dt><code>LevelDict.addDecoration(event : Decoration) -> int:</code>
    <dd>주어진 Decoration(오브젝트)을 레벨에 추가합니다. 해당 장식의 인덱스를 반환합니다.
    <dt><code>LevelDict.getActions(condition : Callable) -> list[Action]:</code>
    <dd>조건에 맞는 모든 Action의 리스트를 반환합니다. 조건이 명시되지 않았을 경우 모든 Action의 리스트를 반환합니다.
    <dt><code>LevelDict.getDecorations(condition : Callable) -> list[Decoration]:</code>
    <dd>조건에 맞는 모든 Decoration의 리스트를 반환합니다. 조건이 명시되지 않았을 경우 모든 장식의 리스트를 반환합니다.
    <dt><code>LevelDict.removeActions(condition : Callable) -> list[Action]:</code>
    <dd>조건에 맞는 모든 Action을 삭제합니다. 삭제한 모든 Action의 리스트를 반환합니다.
    <dt><code>LevelDict.removeDecorations(condition : Callable) -> list[Decoration]:</code>
    <dd>조건에 맞는 모든 Decoration을 삭제합니다. 삭제한 모든 장식의 리스트를 반환합니다.
    <dt><code>LevelDict.popAction(tile, index) -> Action:</code>
    <dd>지정된 타일에 지정된 인덱스를 가진 Action을 삭제합니다. 삭제된 이벤트를 반환합니다.
    <dt><code>LevelDict.popDecoration(tile, index) -> Decoration:</code>
    <dd>지정된 타일에 지정된 인덱스를 가진 Decoration을 삭제합니다. 삭제된 장식을 반환합니다.
    <dt><code>LevelDict.replaceFieldAction(condition : Callable, field : str, new) -> None:</code>
    <dd>조건에 맞는 모든 Action의 "field"의 값을 "new"로 변환합니다.
    <dt><code>LevelDict.replaceFieldDecoration(condition : Callable, field : str, new) -> None:</code>
    <dd>조건에 맞는 모든 Decoration의 "field"의 값을 "new"로 변환합니다.
    <dt><code>LevelDict.writeDictToFile(leveldict : dict, filename : str):</code>
    <dd>ADOFAI 커스텀 레벨 파일에 대응되는 주어진 딕셔너리를 지정된 파일에 덮어씌웁니다. 파일명이 지정되지 않았을 경우 원래 파일을 덮어씌웁니다.
    <br><i><code>LevelDict.leveldict</code>를 사용할 경우 해당 코드를 사용하세요.</i>
    <dt><code>LevelDict.writeToFile(filename : str=None) -> None:</code>
    <dd>LevelDict 오브젝트에 저장된 ADOFAI 커스텀 레벨 파일을 지정된 파일에 덮어씌웁니다. 파일명이 지정되지 않았을 경우 원래 파일을 덮어씌웁니다.
</dl>
<hr>
<i><code style="color : white">Settings</code></i><br>
LevelDict 오브젝트의 일부분입니다. <code>Settings</code> 오브젝트는 <code>dict</code>와 같이 행동합니다. 이 딕셔너리의 키는 ADOFAI 커스텀 레벨 파일의 <code>settings</code>(설정)의 키와 동일한 값을 가집니다.
<hr>
<i><code style="color : white">Tile</code></i><br>
각 Tile을 담은 리스트가 LevelDict 오브젝트 안에 포함되어 있습니다.
<dl>
    <dt><code>Tile.angle : float</code>
    <dd>특정 타일이 보고 있는 방향입니다. (0도가 3시 방향, 90도가 12시 방향)
    <dt><code>Tile.actions : list[Action]</code>
    <dd>특정 타일에 있는 모든 Action을 담은 리스트입니다.
    <dt><code>Tile.decorations : list[Decoration]</code>
    <dd>특정 타일에 있는 모든 장식을 담은 리스트입니다.
</dl>
<hr>
<i><code style="color : white">Action</code></i><br>
타일 위에 놓이는 이벤트가 해당됩니다(보라색 아이콘으로 확인 가능). <code>Action</code> 오브젝트는 <code>dict</code>와 같이 행동합니다. 이 딕셔너리의 키는 이벤트의 종류에 따라 달라집니다. ADOFAI 커스텀 레벨 파일을 열어 원하는 종류의 이벤트의 <code>Actions</code>을 찾아 각 키를 확인할 수 있습니다.
<br><br>
Action 오브젝트는 <code>Tile</code> 오브젝트 안에서 리스트의 형태로 나열되어 있습니다.
<hr>
<i><code style="color : white">Decoration</code></i><br>
왼쪽 사이드바의 장식 탭에서 확인할 수 있는 모든 오브젝트가 해당됩니다. <code>Decoration</code> 오브젝트는 <code>dict</code>와 같이 행동합니다. 이 딕셔너리의 키는 이벤트의 종류에 따라 달라집니다. ADOFAI 커스텀 레벨 파일을 열어 원하는 종류의 장식의 <code>decorations</code>을 찾아 각 키를 확인할 수 있습니다.
<br><br>
Decoration 오브젝트는 <code>Tile</code> 오브젝트 안에 리스트의 형태로 나열되어 있습니다. 만약 장식이 어떠한 타일에도 대응되지 않을 경우, LevelDict.nonFloorDecos 안에 리스트의 형태로 나열되어 있습니다.
<hr><br>