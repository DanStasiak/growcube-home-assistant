@service
def set_state(entity_id=None, **kwargs):
    if not entity_id:
        log.error("Missing 'entity_id' in call to set_state")
        return

    current = state.get(entity_id)
    if current is None:
        log.warning(f"Entity {entity_id} does not exist")
        return

    # Set new attributes, keep current state
    state.set(entity_id, current, **kwargs)
