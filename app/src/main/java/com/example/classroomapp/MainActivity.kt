package com.example.classroomapp


import com.example.classroomapp.R
import android.os.Bundle
import android.view.LayoutInflater
import android.widget.LinearLayout
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.cardview.widget.CardView
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {
    protected override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Находим корневой контейнер для добавления классных комнат
        val container: LinearLayout = findViewById(R.id.container_classrooms)


        // Создаем классные комнаты с разными цветами
        createClassroom(container, "Red classroom (201)", R.color.red_classroom)
        createClassroom(container, "White classroom (202)", R.color.white_classroom)
        createClassroom(container, "Grey classroom (203)", R.color.grey_classroom)
        createClassroom(container, "Green classroom (204)", R.color.green_classroom)
    }

    private fun createClassroom(container: LinearLayout, name: String?, colorResourceId: Int) {
        // Используем LayoutInflater для создания карточки из XML макета
        val inflater = LayoutInflater.from(this)
        val cardView: CardView = inflater.inflate(R.layout.classroom_card, container, false) as CardView


        // Устанавливаем цвет фона
        cardView.setCardBackgroundColor(ContextCompat.getColor(this, colorResourceId))


        // Находим TextView для имени внутри карточки и устанавливаем текст
        val textView: androidx.appcompat.widget.AppCompatTextView = cardView.findViewById(R.id.text_classroom)
        textView.setText(name)


        // Устанавливаем обработчик нажатия
        cardView.setOnClickListener({ view ->
            Toast.makeText(this@MainActivity, "Открыта комната: " + name, Toast.LENGTH_SHORT).show()
        })


        // Добавляем карточку в контейнер
        container.addView(cardView)
    }
}