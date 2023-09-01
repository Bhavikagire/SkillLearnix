import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InstructorService {

  private baseUrl = 'http://127.0.0.1:8000'; // Update this with your Django backend URL

  constructor(private http: HttpClient) { }

  getInstructors(): Observable<any> {
    return this.http.get(`${this.baseUrl}/instructors/`);
  }

  createInstructor(instructorData: any): Observable<any> {
    // Set withCredentials to true to include CSRF token
    return this.http.post(`${this.baseUrl}/instructors/`, instructorData, { withCredentials: true });
  }
  

  // Other CRUD methods...
}
