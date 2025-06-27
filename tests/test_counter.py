from nicegui.testing import User
from nicegui import ui

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    
    # Check that the counter display shows 0 initially
    await user.should_see('0')

async def test_counter_increment(user: User) -> None:
    """Test increment functionality"""
    await user.open('/')
    
    # Click the increment button
    user.find(marker='increment').click()
    
    # Check that counter increased to 1
    await user.should_see('1')

async def test_counter_decrement(user: User) -> None:
    """Test decrement functionality"""
    await user.open('/')
    
    # First increment to have a positive number
    user.find(marker='increment').click()
    await user.should_see('1')
    
    # Now click decrement button
    user.find(marker='decrement').click()
    
    # Check that counter is back to 0
    await user.should_see('0')

async def test_counter_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Increment 3 times
    for _ in range(3):
        user.find(marker='increment').click()
    
    # Check value is 3
    await user.should_see('3')
    
    # Decrement 2 times
    for _ in range(2):
        user.find(marker='decrement').click()
    
    # Check value is 1
    await user.should_see('1')

async def test_counter_negative_values(user: User) -> None:
    """Test that counter can go negative"""
    await user.open('/')
    
    # Click decrement button to go negative
    user.find(marker='decrement').click()
    
    # Check value is -1
    await user.should_see('-1')

async def test_counter_ui_elements(user: User) -> None:
    """Test that all UI elements are present"""
    await user.open('/')
    
    # Check title is present
    await user.should_see('Simple Counter')
    
    # Check both buttons are present using markers
    await user.should_see(marker='increment')
    await user.should_see(marker='decrement')
    
    # Check initial counter value
    await user.should_see('0')