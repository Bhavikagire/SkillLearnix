// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';
// import { Instructor } from './instructor.model';

// @Injectable({
//   providedIn: 'root',
// })
// export class InstructorService {
//   private baseUrl = 'http://localhost:8000/instructors/'; // Replace with your backend URL

//   constructor(private http: HttpClient) {}

//   getInstructors(): Observable<Instructor[]> {
//     return this.http.get<Instructor[]>(this.baseUrl);
//   }

//   getInstructor(id: number): Observable<Instructor> {
//     const url = `${this.baseUrl}${id}/`;
//     return this.http.get<Instructor>(url);
//   }

//   createInstructor(instructor: Instructor): Observable<Instructor> {
//     return this.http.post<Instructor>(this.baseUrl, instructor);
//   }
  
  

//   updateInstructor(id: number, instructor: Instructor): Observable<Instructor> {
//     const url = `${this.baseUrl}${id}/`;
//     return this.http.put<Instructor>(url, instructor);
//   }

//   deleteInstructor(id: number): Observable<void> {
//     const url = `${this.baseUrl}${id}/`;
//     return this.http.delete<void>(url);
//   }
// }

// instructor.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InstructorService {
  private baseUrl = 'http://localhost:8000/'; // Your Django backend URL

  constructor(private http: HttpClient) { }

  createInstructor(instructorData: any): Observable<any> {
    const url = `${this.baseUrl}instructors/create/`;
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getCookie('csrftoken') // Get the CSRF token from the cookie
    });

    return this.http.post(url, instructorData, { headers });
  }

  // Utility function to get a cookie by name
  private getCookie(name: string): string {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()!.split(';').shift()!;
    return '';
  }
}
