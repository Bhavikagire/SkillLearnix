import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { InstructorService } from '../instructor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-instructor-create',
  templateUrl: './instructor-create.component.html',
  styleUrls: ['./instructor-create.component.css']
})
export class InstructorCreateComponent {
  instructor: any = {}; // Define the instructor object

  constructor(private instructorService: InstructorService, private router: Router) {}

  createInstructor(form: NgForm) {
    if (form.valid) {
      this.instructorService.createInstructor(this.instructor).subscribe(
        () => {
          console.log('Instructor created successfully');
          this.router.navigate(['/instructor-list']); // Redirect to instructor list
        },
        (error) => {
          console.error('Error creating instructor:', error);
        }
      );
    }
  }
}
