import axios from 'axios';
import type { Todo } from './types';

const API_URL = 'http://localhost:8001';

export const api = {
  getTodos: () => axios.get<Todo[]>(`${API_URL}/todos`),
  getTodo: (id: number) => axios.get<Todo>(`${API_URL}/todos/${id}`),
  createTodo: (todo: Omit<Todo, 'id'>) => axios.post<Todo>(`${API_URL}/todos`, todo),
  updateTodo: (id: number, todo: Partial<Todo>) => axios.put<Todo>(`${API_URL}/todos/${id}`, todo),
  deleteTodo: (id: number) => axios.delete(`${API_URL}/todos/${id}`),
};
