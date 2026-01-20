import pytest


@pytest.mark.asyncio
async def test_checkout_flow():
    """Integration test: checkout -> outbox -> worker."""
    # TODO: Setup test DB
    # TODO: POST /checkout
    # TODO: Verify order created
    # TODO: Verify inventory decremented
    # TODO: Verify outbox message created
    pass
