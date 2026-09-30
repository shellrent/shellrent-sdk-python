# CLAUDE.md

SDK Python ufficiale delle API pubbliche Shellrent (`shellrent-sdk`, package `shellrent_sdk`): client generato
da `spec/openapi.yaml`; a mano solo autenticazione, creazione del client, CLI, test, documentazione e CI.

## Generato e scritto a mano

- Generato: tutto `src/shellrent_sdk/client/`. Non si modifica mai a mano: `bin/generate` lo cancella e lo ricrea.
- Scritto a mano: il resto di `src/shellrent_sdk/`, `tests/`, `bin/generate`, `openapi-python-client.yaml`,
  `pyproject.toml`, README, CHANGELOG, CI.
- Per cambiare il codice generato, in quest'ordine: opzioni in `openapi-python-client.yaml`,
  `content_type_overrides`, template custom (ultima risorsa: dalla 0.29 si rompono a ogni aggiornamento).

## Rigenerazione

- `bin/generate` (serve uv) esegue con `uvx` openapi-python-client e ruff, con le versioni fissate nello
  script. `--fail-on-warning`: un'operazione non gestita blocca la generazione invece di sparire dal client.
- I post-hook del generatore (ruff) usano `[tool.ruff]` di `pyproject.toml`: se lo cambi, rigenera.
- Per aggiornare il generatore: cambia `GENERATOR_VERSION` (ed eventualmente `RUFF_VERSION`), lancia
  `bin/generate`, rivedi il diff, confronta `requires-python` e dipendenze con quelle che il generatore
  dichiarerebbe (prova con `--meta uv` in una cartella temporanea), lancia i test, annota in `CHANGELOG.md`.
- `spec/openapi.yaml` è una copia della spec dell'applicazione Shellrent: qui non si modifica. I problemi si
  correggono nell'applicazione e poi si ricopia il file.

## Versionamento e rilascio

- SemVer dai tag git (hatch-vcs: niente versione in `pyproject.toml`). Nuove operazioni o modelli: minor.
  operationId o modelli rinominati o rimossi: major, perché cambiano moduli e classi. Nel diff controlla anche
  le firme generate: parametri di path posizionali, gli altri keyword-only; un parametro rinominato o un
  parametro di path aggiunto o spostato è una major.
- Ogni modifica va in `CHANGELOG.md` (Keep a Changelog, sezione `[Unreleased]`).
- Rilascio: tag `vX.Y.Z` (versione PEP 440 normalizzata, come `v1.2.0` o `v1.3.0rc1`) → `release.yml` builda
  e verifica che la versione coincida col tag → il job `publish` attende l'approvazione dell'environment
  `pypi` → Trusted Publishing, senza token. Non rinominare `release.yml`: PyPI lo riconosce per nome.

## Test e verifica

- `uv sync`, poi `uv run ruff format`, `uv run ruff check`, `uv run mypy` (strict, senza il codice generato)
  e `uv run pytest`.
- `tests/support.py`: API finta per `httpx.MockTransport`, orologio finto, `Sleeps` (retry senza dormire).
  `tests/servers.py`: proxy e server HTTPS locali; i certificati di `tests/fixtures/tls` scadono nel 2126 e la
  chiave della CA non è conservata: per rifarli crea una nuova CA e aggiorna `CA_HASH_NAME`.
- `tests/integration` chiama l'API reale solo con `SHELLRENT_CLIENT_ID` e `SHELLRENT_CLIENT_SECRET` (e
  opzionalmente `SHELLRENT_API_URL`); `test_errors.py` richiede lo scope `purchases:read`.
- La CI esegue ruff, mypy e pytest su Python 3.11-3.14, gli stessi controlli su 3.11 con le dipendenze minime
  (`uv sync --resolution lowest-direct`) e `bin/generate`, fallendo se il codice rigenerato è diverso.

## Vincoli

- Python minimo 3.11, come il codice generato. Dipendenze di runtime: solo quelle del codice generato (httpx,
  attrs) con gli stessi limiti. Niente nuove dipendenze senza un motivo forte.
- Il client secret non deve mai finire in cache, nei log, nei messaggi d'errore o nell'output della CLI; la CLI
  lo legge solo dall'ambiente, mai da un'opzione.
- `auth.py`, `http.py` e `cli.py` non importano nulla da `shellrent_sdk.client` (lo verifica `test_layers.py`).
- I transport di default di `RetryTransport` seguono l'ambiente come quelli di httpx: proxy con
  `urllib.request.getproxies`/`proxy_bypass` (httpx non ha un'API pubblica), certificati con `trust_env`.
- L'interfaccia pubblica di `auth`, `http` e della CLI (`main(argv)`, comandi, variabili d'ambiente, exit
  code) è usata da `shellrent-internal-sdk`: cambiarla è una modifica incompatibile (major).
- `create_client()` restituisce `AuthenticatedClient` perché le funzioni generate lo richiedono nel tipo; il
  token lo mette `OAuth2Auth` a ogni richiesta, non il campo `token` del client.
