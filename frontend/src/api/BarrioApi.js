import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api"

export default class BarrioApi {
    static async fetchBarrios() {
        const response = await axios.get(`${API_BASE_URL}/barrios/`)
        return response.data
        }
    }