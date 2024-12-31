# Action Trees


**Source Code**: [https://gitlab.com/roxautomation/action-trees](https://gitlab.com/roxautomation/action-trees)

---

## Summary

**Action Trees** is an `asyncio`-based Python library for managing hierarchical and asynchronous tasks. It breaks down complex tasks into simpler, independent steps that can be run sequentially or in parallel.

## Functionality

- **`ActionItem` Class**: Central class for representing tasks, supporting states like `INITIALIZING`, `RUNNING`, `PAUSED`, and `FAILED`.
- **Task Management**: Provides APIs to start, pause, resume, and cancel tasks asynchronously.
- **Hierarchical Actions**: Actions can have child actions, supporting structured, tree-like task management.
- **Parallel Execution**: Supports running child tasks concurrently using `asyncio`.
- **State and Exception Handling**: Handles task state transitions and exceptions, ensuring proper state flow.

## Example

The following example illustrates a high-level task to prepare and make a cappuccino using the `ActionItem` class:

```python
import asyncio
from action_trees import ActionItem

class AtomicAction(ActionItem):
    """Basic machine action with no children."""
    def __init__(self, name: str, duration: float = 0.1):
        super().__init__(name=name)
        self._duration = duration

    async def _on_run(self) -> None:
        await asyncio.sleep(self._duration)

class PrepareMachineAction(ActionItem):
    """Prepare the machine."""
    def __init__(self) -> None:
        super().__init__(name="prepare")
        self.add_child(AtomicAction(name="initialize"))
        self.add_child(AtomicAction(name="clean"))

    async def _on_run(self) -> None:
        for child in self.children:
            await child.start()

class MakeCappuccinoAction(ActionItem):
    """Make cappuccino."""
    def __init__(self) -> None:
        super().__init__(name="make_cappuccino")
        self.add_child(AtomicAction(name="boil_water"))
        self.add_child(AtomicAction(name="grind_coffee"))

    async def _on_run(self) -> None:
        await self.run_children_parallel()

class CappuccinoOrder(ActionItem):
    """High-level action to make a cappuccino."""
    def __init__(self) -> None:
        super().__init__(name="cappuccino_order")
        self.add_child(PrepareMachineAction())
        self.add_child(MakeCappuccinoAction())

    async def _on_run(self) -> None:
        for child in self.children:
            await child.start()

async def main() -> None:
    order = CappuccinoOrder()
    await order.start()
    order.display_tree()

if __name__ == "__main__":
    asyncio.run(main())
```

This code creates a hierarchical task to prepare a machine and make a cappuccino, with some actions running sequentially and others in parallel.


**More examples** : see [examples](https://gitlab.com/roxautomation/action-trees/-/tree/main/examples?ref_type=heads)


## State transitions

`ActionItem` contains a state machine with these transitions. (spec from VDA5050)

![](docs/img/Figure14.png)
