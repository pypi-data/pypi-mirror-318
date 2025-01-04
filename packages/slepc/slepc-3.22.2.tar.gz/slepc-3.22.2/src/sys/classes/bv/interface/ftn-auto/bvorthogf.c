#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* bvorthog.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcbv.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvorthogonalizevec_ BVORTHOGONALIZEVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvorthogonalizevec_ bvorthogonalizevec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvorthogonalizecolumn_ BVORTHOGONALIZECOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvorthogonalizecolumn_ bvorthogonalizecolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvorthonormalizecolumn_ BVORTHONORMALIZECOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvorthonormalizecolumn_ bvorthonormalizecolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvorthogonalizesomecolumn_ BVORTHOGONALIZESOMECOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvorthogonalizesomecolumn_ bvorthogonalizesomecolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvorthogonalize_ BVORTHOGONALIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvorthogonalize_ bvorthogonalize
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  bvorthogonalizevec_(BV bv,Vec v,PetscScalar *H,PetscReal *norm,PetscBool *lindep, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(v);
CHKFORTRANNULLSCALAR(H);
CHKFORTRANNULLREAL(norm);
*ierr = BVOrthogonalizeVec(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((v) ),H,norm,lindep);
}
SLEPC_EXTERN void  bvorthogonalizecolumn_(BV bv,PetscInt *j,PetscScalar *H,PetscReal *norm,PetscBool *lindep, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLSCALAR(H);
CHKFORTRANNULLREAL(norm);
*ierr = BVOrthogonalizeColumn(
	(BV)PetscToPointer((bv) ),*j,H,norm,lindep);
}
SLEPC_EXTERN void  bvorthonormalizecolumn_(BV bv,PetscInt *j,PetscBool *replace,PetscReal *norm,PetscBool *lindep, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLREAL(norm);
*ierr = BVOrthonormalizeColumn(
	(BV)PetscToPointer((bv) ),*j,*replace,norm,lindep);
}
SLEPC_EXTERN void  bvorthogonalizesomecolumn_(BV bv,PetscInt *j,PetscBool *which,PetscScalar *H,PetscReal *norm,PetscBool *lindep, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLSCALAR(H);
CHKFORTRANNULLREAL(norm);
*ierr = BVOrthogonalizeSomeColumn(
	(BV)PetscToPointer((bv) ),*j,which,H,norm,lindep);
}
SLEPC_EXTERN void  bvorthogonalize_(BV V,Mat R, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(R);
*ierr = BVOrthogonalize(
	(BV)PetscToPointer((V) ),
	(Mat)PetscToPointer((R) ));
}
#if defined(__cplusplus)
}
#endif
