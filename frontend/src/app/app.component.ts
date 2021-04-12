import { Component } from '@angular/core';
import {HttpClient, HttpEvent, HttpErrorResponse, HttpEventType} from '@angular/common/http';
import {DomSanitizer, SafeUrl} from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'remtech';
  fileName = '';
  path: SafeUrl = '';
  w = 0;
  h = 0;

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {
  }
  onFileSelected(event): void {
    const file: File = event.target.files[0];
    if (file) {
      this.fileName = file.name;
      const formData = new FormData();
      formData.append('thumbnail', file);
      const upload = this.http.post('http://127.0.0.1:8000/object_detection/', formData);
      upload.subscribe(data => {
        this.path = this.sanitizer.bypassSecurityTrustResourceUrl(`data:image/png;base64, ${data['image']}`);
        this.w = data['w'];
        this.h = data['h'];
      });
      console.log('Hey!');
    }
  }

}
