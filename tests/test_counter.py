from nicegui.testing import User
from nicegui import ui, app

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0 for new users."""
    await user.open('/')
    await user.should_see('Count: 0')
    await user.should_see('Simple Counter')

async def test_counter_increment(user: User) -> None:
    """Test increment functionality."""
    await user.open('/')
    
    # Click increment button
    user.find('Increment (+1)').click()
    await user.should_see('Count: 1')
    
    # Click increment again
    user.find('Increment (+1)').click()
    await user.should_see('Count: 2')

async def test_counter_decrement(user: User) -> None:
    """Test decrement functionality."""
    await user.open('/')
    
    # First increment to have a positive number
    user.find('Increment (+1)').click()
    await user.should_see('Count: 1')
    
    # Then decrement
    user.find('Decrement (-1)').click()
    await user.should_see('Count: 0')
    
    # Decrement below zero
    user.find('Decrement (-1)').click()
    await user.should_see('Count: -1')

async def test_counter_reset(user: User) -> None:
    """Test reset functionality."""
    await user.open('/')
    
    # Increment a few times
    user.find('Increment (+1)').click()
    user.find('Increment (+1)').click()
    user.find('Increment (+1)').click()
    await user.should_see('Count: 3')
    
    # Reset counter
    user.find('Reset').click()
    await user.should_see('Count: 0')

async def test_counter_mixed_operations(user: User) -> None:
    """Test mixed increment/decrement operations."""
    await user.open('/')
    
    # Perform mixed operations
    user.find('Increment (+1)').click()  # 1
    user.find('Increment (+1)').click()  # 2
    user.find('Decrement (-1)').click()  # 1
    user.find('Increment (+1)').click()  # 2
    user.find('Decrement (-1)').click()  # 1
    user.find('Decrement (-1)').click()  # 0
    user.find('Decrement (-1)').click()  # -1
    
    await user.should_see('Count: -1')

async def test_counter_buttons_exist(user: User) -> None:
    """Test that all required buttons are present."""
    await user.open('/')
    
    # Check that all buttons exist
    await user.should_see('Increment (+1)')
    await user.should_see('Decrement (-1)')
    await user.should_see('Reset')