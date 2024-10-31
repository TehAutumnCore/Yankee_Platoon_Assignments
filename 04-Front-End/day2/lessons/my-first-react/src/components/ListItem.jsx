import { useState } from "react";

const ListItem = ({ task, handleCheck }) => {
  const [isCompleted, setIsCompleted] = useState(task.completed);

  // if check is true
  return (
    <li>
      {task.task}
      <input
        type="checkbox"
        checked={isCompleted}
        onChange={(e) =>
          e.target.checked
            ? handleCheck(task)
            : setIsCompleted(e.target.checked)
        }
      />
    </li>
  );
};

export default ListItem;