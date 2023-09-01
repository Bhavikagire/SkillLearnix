import { Component } from '@angular/core';
import { InstructorService } from '../instructor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-instructor-create',
  templateUrl: './instructor-create.component.html',
  styleUrls: ['./instructor-create.component.css']
})
export class InstructorCreateComponent {
  instructor: any = {}; // Initialize an empty object to hold instructor data

  constructor(private instructorService: InstructorService, private router: Router) {}

  onSubmit() {
    this.instructorService.createInstructor(this.instructor).subscribe(
      (data) => {
        console.log('Instructor created successfully:', data);
        // Optionally, you can navigate to the instructor list or show a success message here.
        this.router.navigate(['/instructors']);
      },
      (error) => {
        console.error('Error creating instructor:', error);
        // Handle errors and show an error message if needed.
      }
    );
  }
}
