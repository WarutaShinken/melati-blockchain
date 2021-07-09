from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "melati_harvester melati_timelord_launcher melati_timelord melati_farmer melati_full_node melati_wallet".split(),
    "node": "melati_full_node".split(),
    "harvester": "melati_harvester".split(),
    "farmer": "melati_harvester melati_farmer melati_full_node melati_wallet".split(),
    "farmer-no-wallet": "melati_harvester melati_farmer melati_full_node".split(),
    "farmer-only": "melati_farmer".split(),
    "timelord": "melati_timelord_launcher melati_timelord melati_full_node".split(),
    "timelord-only": "melati_timelord".split(),
    "timelord-launcher-only": "melati_timelord_launcher".split(),
    "wallet": "melati_wallet melati_full_node".split(),
    "wallet-only": "melati_wallet".split(),
    "introducer": "melati_introducer".split(),
    "simulator": "melati_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
