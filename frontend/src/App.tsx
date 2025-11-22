import { useState, useEffect } from 'react';
import { api } from './api';
import type { Todo } from './types';
import './App.css';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTitle, setNewTitle] = useState('');
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editTitle, setEditTitle] = useState('');

  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    const response = await api.getTodos();
    setTodos(response.data);
  };

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;
    await api.createTodo({ title: newTitle, done: false });
    setNewTitle('');
    loadTodos();
  };

  const handleToggle = async (todo: Todo) => {
    await api.updateTodo(todo.id, { ...todo, done: !todo.done });
    loadTodos();
  };

  const handleDelete = async (id: number) => {
    await api.deleteTodo(id);
    loadTodos();
  };

  const handleEdit = (todo: Todo) => {
    setEditingId(todo.id);
    setEditTitle(todo.title);
  };

  const handleSaveEdit = async (id: number) => {
    await api.updateTodo(id, { title: editTitle, done: todos.find(t => t.id === id)?.done || false });
    setEditingId(null);
    loadTodos();
  };

  const completedCount = todos.filter(t => t.done).length;
  const pendingCount = todos.filter(t => !t.done).length;

  return (
    <div className="app">
      <header className="header">
        <h1>Reminders</h1>
        <div className="stats">
          <span className="stat pending">{pendingCount} Pending</span>
          <span className="stat completed">{completedCount} Completed</span>
        </div>
      </header>

      <form className="add-form" onSubmit={handleAdd}>
        <input
          type="text"
          placeholder="Add a new reminder..."
          value={newTitle}
          onChange={(e) => setNewTitle(e.target.value)}
        />
        <button type="submit">+</button>
      </form>

      <ul className="todo-list">
        {todos.map((todo) => (
          <li key={todo.id} className={`todo-item ${todo.done ? 'done' : ''}`}>
            <button
              className={`checkbox ${todo.done ? 'checked' : ''}`}
              onClick={() => handleToggle(todo)}
            >
              {todo.done && '✓'}
            </button>

            {editingId === todo.id ? (
              <input
                className="edit-input"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                onBlur={() => handleSaveEdit(todo.id)}
                onKeyDown={(e) => e.key === 'Enter' && handleSaveEdit(todo.id)}
                autoFocus
              />
            ) : (
              <span className="title" onDoubleClick={() => handleEdit(todo)}>
                {todo.title}
              </span>
            )}

            <button className="delete-btn" onClick={() => handleDelete(todo.id)}>
              ×
            </button>
          </li>
        ))}
      </ul>

      {todos.length === 0 && (
        <p className="empty">No reminders yet. Add one above!</p>
      )}
    </div>
  );
}

export default App;
