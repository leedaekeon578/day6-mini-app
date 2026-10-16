# app.py 계획 (uv 환경)

## Context
할 일을 우선순위 순서로 보여 주는 Python 터미널 앱. app.py 초안은 이미 있으나 이 컴퓨터에 실제 Python이 없어(Windows Store 스텁) 실행 확인을 못 했다. uv로 Python을 준비해 확인한다.

## 읽은 파일
- AGENTS.md
- app.py (초안 45줄. 숫자 우선순위, 메모리 저장, 추가·목록, 동점 시 입력 순서 유지)

## 만들거나 수정할 파일
- 만들기: 없음
- 수정: 없음 (app.py는 현재 계획에 맞음. 확인 중 버그가 나오면 app.py만 최소 수정)
- uv가 `.venv`, `pyproject.toml` 등을 만들 수 있어 `uv run`만 사용하고 `uv init`/`uv venv`는 쓰지 않음

## 구현할 함수 (이미 구현됨)
- `main()`, `add_task(tasks, title, priority)`, `sort_tasks(tasks)`, `show_tasks(tasks)`, `ask_priority()`

## 실행할 확인 명령 (PowerShell)
1. `uv --version` (uv 설치 확인. 없으면 설치 여부를 먼저 물어봄)
2. `uv python list --only-installed` (설치된 Python 확인. 없으면 `uv python install`, 아래 질문 1)
3. `uv run python --version`
4. `"1`nB`n3`n1`nA`n1`n1`nC`n3`n2`nx`n3" | uv run app.py`
   - 기대 출력: `[1] A`, `[1] C`, `[3] B` 순 (동점 A, C는 입력 순서 유지)
   - 우선순위 `x` 입력 시 "1 이상의 숫자를 입력하세요." 출력 확인

## 결정이 필요한 질문
1. uv가 없거나 Python이 없을 때 `uv python install`로 Python을 내려받아도 되는가? (시스템에 설치 발생)
2. 프로젝트 폴더에 `pyproject.toml`/`.venv`가 생기는 것을 허용하는가? (`uv run app.py`만 쓰면 보통 생기지 않음)
