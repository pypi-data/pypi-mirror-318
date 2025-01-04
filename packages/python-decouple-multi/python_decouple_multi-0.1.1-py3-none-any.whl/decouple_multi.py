'''
Täydennetään `python-decouple`-paketin määrittelemää `AutoConfig`-luokkaa
siten, että se ottaa `search_path`-parametrinä vastaan luettelon tai monikon
halutuista parametritiedostojen hakupoluista:
>>> from decouple_multi import AutoConfig
>>> CONFIG = AutoConfig(
>>>   search_path=(
>>>     '/etc/asetukset/tuotanto',
>>>     '/usr/local/lib/asetukset/tuotanto',
>>>     ...
>>>   )
>>> )

Toteutus on taaksepäin yhteensopiva; `AutoConfig`-luokka voidaan alustaa
myös täsmälleen samoin kuin `decouple.AutoConfig` ja sitä kutsutaan samoin.

Kaikki annetut hakupolut käydään läpi ja kaikki niistä ja niiden isäntä-
hakemistoista löytyneet asetustiedostot luetaan (ei vain ensimmäinen).

Luettelossa ensin annetusta polusta löytyneet tiedostot ylikirjoittavat
myöhemmän polun sisällön; samoin syvemmästä alihakemistosta löytynyt
tiedosto ylikirjoittaa ylempänä hierarkiassa olevan tiedoston.

Em. esimerkkiä noudattaen, jos tiedostot ja niiden sisällöt ovat nämä:
```
(/etc/asetukset/tuotanto/.env)           PARAM_D=L
(/etc/asetukset/.env)                    PARAM_A=N, PARAM_C=P
(/usr/local/lib/asetukset/tuotanto/.env) PARAM_A=X, PARAM_B=Y, PARAM_C=Z
(/usr/local/lib/asetukset/.env)          PARAM_A=J, PARAM_B=K
```

Tuloksena saadaan arvot `PARAM_A=N, PARAM_B=Y, PARAM_C=P, PARAM_D=L`.

Huomaa, että kaikki muu `decouple`-paketin tarjoama sisältö tarjotaan
sellaisenaan myös tässä paketissa.
'''

from decouple import *


class MultiConfig(Config):
  def __init__(self, *tiedostot):
    self.repository = {}
    self.tiedostot = tiedostot

  def get(self, option, default=undefined, cast=undefined):
    value = undefined
    if option in os.environ:
      value = os.environ[option]
    else:
      for tiedosto in self.tiedostot:
        if option in tiedosto:
          value = tiedosto[option]
          break
    if value is undefined:
      if isinstance(default, Undefined):
        return super().get(option)
      value = default
    if isinstance(cast, Undefined):
      cast = self._cast_do_nothing
    elif cast is bool:
      cast = self._cast_boolean
    return cast(value)
    # def get

  # class MultiConfig


class AutoConfig(AutoConfig):

  def __init__(self, search_path=None):
    self.search_path = (
      search_path if isinstance(search_path, (type(None), list, tuple))
      else (search_path, )
    )
    self.config = None
    # def __init__

  def _tiedostot(self, polut):
    def __tiedostot(path):
      ''' Vrt. super()._find_file. '''
      try:
        for configfile in self.SUPPORTED:
          filename = os.path.join(path, configfile)
          if os.path.isfile(filename):
            yield filename
        parent = os.path.dirname(path)
        if parent \
        and os.path.normcase(parent) != os.path.normcase(os.path.abspath(os.sep)):
          yield from __tiedostot(parent)
      except Exception:
        pass
      # def __tiedostot
    for path in polut:
      yield from __tiedostot(path)
    # def _tiedostot

  def _load(self, polut):
    self.config = MultiConfig(*(
      self.SUPPORTED.get(
        os.path.basename(tiedosto),
        RepositoryEmpty
      )(
        tiedosto,
        encoding=self.encoding
      )
      for tiedosto in self._tiedostot(polut)
    ))
    # def _load

  def __call__(self, *args, **kwargs):
    if not self.config:
      self._load(self.search_path + (self._caller_path(), ))
    return self.config(*args, **kwargs)
    # def __call__

  def __repr__(self):
    return (
      f'{self.__class__.__qualname__}'
      f'({", ".join(map(repr, self.search_path))})'
    )
    # def __repr__

  # class AutoConfig
