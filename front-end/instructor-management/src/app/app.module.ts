import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module'; // Import the AppRoutingModule

import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { InstructorComponent } from './instructor/instructor.component';
import { InstructorCreateComponent } from './instructor-create/instructor-create.component';

@NgModule({
  declarations: [AppComponent, InstructorComponent, InstructorCreateComponent],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule,FormsModule, HttpClientXsrfModule.withOptions({
    cookieName: 'csrftoken', // This should match your Django settings
    headerName: 'X-CSRFToken', // This should match your Django settings
  }),],  // Include AppRoutingModule here
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
